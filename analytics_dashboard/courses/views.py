import copy
import datetime
import json
import logging
import requests

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.utils import dateformat
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.utils.translation import ugettext_lazy as _
from braces.views import LoginRequiredMixin

from analyticsclient.constants import data_format, demographic
from analyticsclient.client import Client
from analyticsclient.exceptions import NotFoundError
from courses import permissions
from courses.presenters import CourseEngagementPresenter, CourseEnrollmentPresenter
from courses.utils import is_feature_enabled


logger = logging.getLogger(__name__)


class TrackedViewMixin(object):
    """
    Adds tracking variables to the context passed to Javascript.
    """

    # Page name used for usage tracking/analytics
    page_name = None

    def get_context_data(self, **kwargs):
        context = super(TrackedViewMixin, self).get_context_data(**kwargs)
        context['js_data'] = context.get('js_data', {})
        context['js_data'].update({
            'tracking': {
                'segmentApplicationId': settings.SEGMENT_IO_KEY,  # None will translate to 'null'
                'page': self.page_name
            }
        })
        return context


class CourseContextMixin(TrackedViewMixin):
    """
    Adds default course context data.

    Use primarily with templated views where data needs to be passed to Javascript.
    """
    # Title displayed on the page
    page_title = None
    page_subtitle = None

    def get_context_data(self, **kwargs):
        context = super(CourseContextMixin, self).get_context_data(**kwargs)
        context.update(self.get_default_data())

        context['js_data'] = context.get('js_data', {})
        user = self.request.user
        context['js_data'].update({
            'course': {
                'courseId': self.course_id
            },
            'user': {
                'userId': user.get_username(),
                'userName': user.get_full_name(),
                'userEmail': user.email,
            },
        })

        return context

    def get_default_data(self):
        """
        Returns default data for the pages (context and javascript data).
        """
        context = {
            'course_id': self.course_id,
            'page_title': self.page_title,
            'page_subtitle': self.page_subtitle
        }

        return context


class CourseValidMixin(object):
    """
    Mixin that checks the validity of a course ID against the LMS.
    """

    course_id = None

    def is_valid_course(self):

        if settings.LMS_COURSE_VALIDATION_BASE_URL:
            uri = '{0}/{1}/info'.format(settings.LMS_COURSE_VALIDATION_BASE_URL, self.course_id)

            try:
                response = requests.get(uri, timeout=5)
            except requests.exceptions.Timeout:
                logger.error('Course validation timed out: {}'.format(uri))
                # consider the course valid if the LMS times out
                return True

            # pylint: disable=no-member
            return response.status_code == requests.codes.ok
        else:
            # all courses valid if LMS url isn't specified
            return True

    def dispatch(self, request, *args, **kwargs):
        if self.is_valid_course():
            return super(CourseValidMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404


class CoursePermissionMixin(object):
    course_id = None
    user = None

    def can_view(self):
        return permissions.user_can_view_course(self.user, self.course_id)

    def dispatch(self, request, *args, **kwargs):
        if settings.ENABLE_COURSE_PERMISSIONS and not self.can_view():
            raise PermissionDenied

        return super(CoursePermissionMixin, self).dispatch(request, *args, **kwargs)


class CourseNavBarMixin(object):
    """
    Mixin to add navbar items to context.

    This mixin is intended for course views that have a course_id property.
    """

    # Primary nav item that should be displayed as active. This value MUST be overwritten by the child class.
    active_primary_nav_item = None

    # Secondary nav item that should be displayed as active. This value is optional.
    active_secondary_nav_item = None

    # Items that will populate the secondary nav list. This value is optional.
    secondary_nav_items = []

    def get_primary_nav_items(self):
        """
        Return the primary nav items.
        """

        items = [
            {
                'name': 'enrollment',
                'label': _('Enrollment'),
                'view': 'courses:enrollment_activity',
                'icon': 'fa-child'
            },
            {
                'name': 'engagement',
                'label': _('Engagement'),
                'view': 'courses:engagement_content',
                'icon': 'fa-bar-chart',
            }
        ]

        # Remove disabled items
        items = filter(is_feature_enabled, items)

        # Clean each item
        map(self.clean_item, items)

        return items

    def get_secondary_nav_items(self):
        """
        Return the secondary nav items.
        """

        # Deep copy the list since it is a list of dictionaries
        items = copy.deepcopy(self.secondary_nav_items)

        # Process only the nav items that are enabled
        items = filter(is_feature_enabled, items)

        for item in items:
            item['active'] = self.active_secondary_nav_item == item['name']
            self.clean_item(item)

        return items

    def clean_item(self, item):
        """
        Remove extraneous keys from item and set the href value.
        """
        # Prevent page reload if user clicks on the active navbar item, otherwise navigate to the new page.
        if item.get('active', False):
            href = '#'
        else:
            href = reverse(item['view'], kwargs={'course_id': self.course_id})

        item['href'] = href

        # Delete entries that are no longer needed
        item.pop('view', None)
        item.pop('switch', None)

    def get_context_data(self, **kwargs):
        context = super(CourseNavBarMixin, self).get_context_data(**kwargs)

        primary_nav_items = self.get_primary_nav_items()
        secondary_nav_items = self.get_secondary_nav_items()

        # Get the active primary item and remove it from the list
        primary_nav_item = [i for i in primary_nav_items if i['name'] == self.active_primary_nav_item][0]
        primary_nav_items.remove(primary_nav_item)

        context.update({
            'primary_nav_item': primary_nav_item,
            'primary_nav_items': primary_nav_items,
            'secondary_nav_items': secondary_nav_items
        })

        return context


class CourseView(LoginRequiredMixin, CourseValidMixin, CoursePermissionMixin, TemplateView):
    """
    Base course view.

    Adds conveniences such as course_id attribute, and handles 404s when retrieving data from the API.
    """
    client = None
    course = None
    course_id = None
    user = None

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.course_id = kwargs['course_id']

        # some views will catch the NotFoundError to set data to a state that
        # the template can rendering a loading error message for the section
        try:
            return super(CourseView, self).dispatch(request, *args, **kwargs)
        except NotFoundError:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        self.client = Client(base_url=settings.DATA_API_URL,
                             auth_token=settings.DATA_API_AUTH_TOKEN, timeout=5)
        self.course = self.client.courses(self.course_id)
        return context


class CourseTemplateView(CourseContextMixin, CourseNavBarMixin, CourseView):
    update_message = None

    def get_last_updated_message(self, last_updated):
        if last_updated:
            return self.update_message % self.format_last_updated_date_and_time(last_updated)
        else:
            return None

    @staticmethod
    def format_last_updated_date_and_time(d):
        return {'update_date': dateformat.format(d, settings.DATE_FORMAT), 'update_time': dateformat.format(d, 'g:i A')}


class EnrollmentTemplateView(CourseTemplateView):
    """
    Base view for course enrollment pages.
    """
    secondary_nav_items = [
        {'name': 'activity', 'label': _('Activity'), 'view': 'courses:enrollment_activity'},
        {'name': 'geography', 'label': _('Geography'), 'view': 'courses:enrollment_geography'},
    ]
    active_primary_nav_item = 'enrollment'


class EngagementTemplateView(CourseTemplateView):
    """
    Base view for course engagement pages.
    """
    secondary_nav_items = [
        # Translators: Content as in course content (e.g. things, not the feeling)
        {'name': 'content', 'label': _('Content'), 'view': 'courses:engagement_content'},
    ]
    active_primary_nav_item = 'engagement'


class CSVResponseMixin(object):
    def render_to_response(self, context, **response_kwargs):
        response = HttpResponse(context['data'], content_type='text/csv',
                                **response_kwargs)
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(
            context['filename'])
        return response


class JSONResponseMixin(object):
    def render_to_response(self, context, **response_kwargs):
        content = json.dumps(context['data'])
        return HttpResponse(content, content_type='application/json',
                            **response_kwargs)


class EnrollmentActivityView(EnrollmentTemplateView):
    template_name = 'courses/enrollment_activity.html'
    page_title = _('Enrollment Activity')
    page_name = 'enrollment_activity'
    active_secondary_nav_item = 'activity'

    # Translators: Do not translate UTC.
    update_message = _('Enrollment activity data was last updated %(update_date)s at %(update_time)s UTC.')

    # pylint: disable=line-too-long
    def get_context_data(self, **kwargs):
        context = super(EnrollmentActivityView, self).get_context_data(**kwargs)

        presenter = CourseEnrollmentPresenter(self.course_id)

        summary = None
        trend = None
        last_updated = None
        try:
            summary, trend = presenter.get_summary_and_trend_data()
            last_updated = summary['last_updated']
        except NotFoundError:
            logger.error("Failed to retrieve enrollment activity data for %s.", self.course_id)

        # add the enrollment data for the page
        context['js_data']['course']['enrollmentTrends'] = trend

        context.update({
            'page_data': json.dumps(context['js_data']),
            'summary': summary,
            'update_message': self.get_last_updated_message(last_updated)
        })

        return context


class EnrollmentGeographyView(EnrollmentTemplateView):
    template_name = 'courses/enrollment_geography.html'
    page_title = _('Enrollment Geography')
    page_name = 'enrollment_geography'
    active_secondary_nav_item = 'geography'

    # Translators: Do not translate UTC.
    update_message = _('Geographic student data was last updated %(update_date)s at %(update_time)s UTC.')

    def get_context_data(self, **kwargs):
        context = super(EnrollmentGeographyView, self).get_context_data(**kwargs)

        presenter = CourseEnrollmentPresenter(self.course_id)

        data = None
        last_updated = None
        try:
            summary, data = presenter.get_geography_data()
            last_updated = summary['last_updated']

            # Add summary data (e.g. num countries, top 3 countries) directly to the context
            context.update(summary)
        except NotFoundError:
            logger.error("Failed to retrieve enrollment geography data for %s.", self.course_id)

        context['js_data']['course']['enrollmentByCountry'] = data

        context.update({
            'page_data': json.dumps(context['js_data']),
            'update_message': self.get_last_updated_message(last_updated)
        })

        return context


class EngagementContentView(EngagementTemplateView):
    template_name = 'courses/engagement_content.html'
    page_title = _('Engagement Content')
    page_name = 'engagement_content'
    active_secondary_nav_item = 'content'

    # Translators: Do not translate UTC.
    update_message = _('Course engagement data was last updated %(update_date)s at %(update_time)s UTC.')

    def get_context_data(self, **kwargs):
        context = super(EngagementContentView, self).get_context_data(**kwargs)

        presenter = CourseEngagementPresenter(self.course_id)

        summary = None
        trends = None
        last_updated = None
        try:
            summary, trends = presenter.get_summary_and_trend_data()
            last_updated = summary['last_updated']
        except NotFoundError:
            logger.error("Failed to retrieve engagement content data for %s.", self.course_id)

        context['js_data']['course']['engagementTrends'] = trends
        context.update({
            'summary': summary,
            'page_data': json.dumps(context['js_data']),
            'update_message': self.get_last_updated_message(last_updated)
        })

        return context


class CourseEnrollmentByCountryCSV(CSVResponseMixin, CourseView):
    def get_context_data(self, **kwargs):
        context = super(CourseEnrollmentByCountryCSV, self).get_context_data(**kwargs)

        context.update({
            'data': self.course.enrollment(demographic.LOCATION, data_format=data_format.CSV),
            'filename': '{0}_enrollment_by_country.csv'.format(self.course_id)
        })

        return context


class CourseEnrollmentCSV(CSVResponseMixin, CourseView):
    def get_context_data(self, **kwargs):
        context = super(CourseEnrollmentCSV, self).get_context_data(**kwargs)
        end_date = datetime.datetime.utcnow().strftime(Client.DATE_FORMAT)

        context.update({
            'data': self.course.enrollment(data_format=data_format.CSV, end_date=end_date),
            'filename': '{0}_enrollment.csv'.format(self.course_id)
        })

        return context


class CourseEngagementActivityTrendCSV(CSVResponseMixin, CourseView):
    def get_context_data(self, **kwargs):
        context = super(CourseEngagementActivityTrendCSV, self).get_context_data(**kwargs)
        end_date = datetime.datetime.utcnow().strftime(Client.DATE_FORMAT)

        context.update({
            'data': self.course.activity(data_format=data_format.CSV, end_date=end_date),
            'filename': '{0}_engagement_activity_trend.csv'.format(self.course_id)
        })

        return context


class CourseHome(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        course_id = kwargs['course_id']
        return reverse('courses:enrollment_activity', kwargs={'course_id': course_id})


class CourseIndex(LoginRequiredMixin, TrackedViewMixin, TemplateView):
    template_name = 'courses/index.html'
    page_name = 'course_index'

    def get_context_data(self, **kwargs):
        context = super(CourseIndex, self).get_context_data(**kwargs)

        courses = permissions.get_user_course_permissions(self.request.user)

        if not courses:
            # The user is probably not a course administrator and should not be using this application.
            raise PermissionDenied

        context['courses'] = sorted(courses)

        context.update({
            'page_data': json.dumps(context['js_data']),
        })

        return context
