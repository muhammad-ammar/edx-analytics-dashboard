"""
Tests for course analytics pages
"""

from bok_choy.page_object import PageObject

from acceptance_tests import DASHBOARD_SERVER_URL, auto_auth


class DashboardPage(PageObject):
    path = None

    @property
    def url(self):
        return self.page_url

    def __init__(self, browser, path=None):
        super(DashboardPage, self).__init__(browser)
        path = path or self.path
        self.server_url = DASHBOARD_SERVER_URL
        self.page_url = '{0}/{1}'.format(self.server_url, path)


class CoursePage(DashboardPage):
    def __init__(self, browser, course_id=None):
        # Create the path
        self.course_id = course_id or 'edX/DemoX/Demo_Course'
        path = 'courses/{}'.format(self.course_id)

        # Call the constructor and setup the URL
        super(CoursePage, self).__init__(browser, path)

        # Automatically create and login a new user
        auto_auth(browser, self.server_url)

    def is_browser_on_page(self):
        return self.browser.current_url == self.page_url


class CourseEnrollmentActivityPage(CoursePage):
    def __init__(self, browser, course_id=None):
        super(CourseEnrollmentActivityPage, self).__init__(browser, course_id)
        self.page_url += '/enrollment/activity/'

    def is_browser_on_page(self):
        return super(CourseEnrollmentActivityPage, self).is_browser_on_page() and \
               'Enrollment Activity' in self.browser.title


class LoginPage(DashboardPage):
    path = 'accounts/login'

    def is_browser_on_page(self):
        return True


class CourseEnrollmentGeographyPage(CoursePage):
    def __init__(self, browser, course_id=None):
        super(CourseEnrollmentGeographyPage, self).__init__(browser, course_id)
        self.page_url += '/enrollment/geography/'

    def is_browser_on_page(self):
        return super(CourseEnrollmentGeographyPage, self).is_browser_on_page() and \
               'Enrollment Geography' in self.browser.title


class CourseEngagementContentPage(CoursePage):
    def __init__(self, browser, course_id=None):
        super(CourseEngagementContentPage, self).__init__(browser, course_id)
        self.page_url += '/engagement/content/'

    def is_browser_on_page(self):
        return super(CourseEngagementContentPage, self).is_browser_on_page() and \
               'Engagement Content' in self.browser.title


class CourseIndexPage(DashboardPage):
    path = 'courses/'

    def __init__(self, browser):
        super(CourseIndexPage, self).__init__(browser)

        # Automatically create and login a new user
        auto_auth(browser, self.server_url)

    def is_browser_on_page(self):
        return 'Courses' in self.browser.title


class ErrorPage(DashboardPage):
    error_code = None
    error_title = None

    def __init__(self, browser):
        self.path = self.path or '{}/'.format(self.error_code)
        super(ErrorPage, self).__init__(browser)

    def is_browser_on_page(self):
        element = self.q(css='.error-title')
        return element.present and element.text[0] == self.error_title


class ServerErrorPage(ErrorPage):
    error_code = 500
    error_title = u'An Error Occurred'


class NotFoundErrorPage(ErrorPage):
    error_code = 404
    error_title = u'Page Not Found'


class AccessDeniedErrorPage(ErrorPage):
    error_code = 403
    error_title = u'Access Denied'


class AuthErrorPage(ErrorPage):
    error_title = u'Authentication Failed'
    path = u'auth/error/'
