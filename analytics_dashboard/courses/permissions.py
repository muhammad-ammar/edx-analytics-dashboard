
import datetime
import logging
from django.conf import settings
from django.core.cache import cache
from social.apps.django_app import load_strategy
from analytics_dashboard.backends import EdXOpenIdConnect
from courses.exceptions import UserNotAssociatedWithBackendError, InvalidAccessTokenError, \
    PermissionsRetrievalFailedError

logger = logging.getLogger(__name__)


def _get_course_permission_cache_keys(user):
    """
    Return the cache keys used for user-course permissions
    """
    key_last_updated = 'course_permissions_updated_at_{}'.format(user.pk)
    key_courses = 'course_permissions_{}'.format(user.pk)
    return key_courses, key_last_updated


def set_user_course_permissions(user, courses):
    """
    Sets which courses user is allowed to view.

    Arguments
        user (User)     --  User for which permissions should be set
        courses (list)  --  List of course ID strings
    """
    if not user:
        raise ValueError('User not specified!')

    if courses is None:
        raise ValueError('Courses not specified!')

    # Ensure courses are stored as a list.
    courses = list(courses)

    key_courses, key_last_updated = _get_course_permission_cache_keys(user)

    data = {key_courses: courses, key_last_updated: datetime.datetime.utcnow()}
    cache.set_many(data, settings.COURSE_PERMISSIONS_TIMEOUT)


def revoke_user_course_permissions(user):
    """
    Revokes all course permissions for the given user.

    Arguments
        user (User) --  User for which permissions should be revoked
    """
    cache.delete_many(_get_course_permission_cache_keys(user))


def refresh_user_course_permissions(user):
    """
    Refresh user course permissions from the auth server.

    Arguments
        user (User) --  User whose permissions should be refreshed
    """
    backend = EdXOpenIdConnect(strategy=load_strategy())
    user_social_auth = user.social_auth.filter(provider=backend.name).first()

    if not user_social_auth:
        raise UserNotAssociatedWithBackendError

    access_token = user_social_auth.extra_data.get('access_token')

    if not access_token:
        raise InvalidAccessTokenError

    try:
        claims = settings.COURSE_PERMISSIONS_CLAIMS
        data = backend.get_user_claims(access_token, claims)
        courses = set()
        for claim in claims:
            courses.update(data.get(claim, []))
    except Exception as e:
        raise PermissionsRetrievalFailedError(e)

    # If the backend does not provide course permissions, assign no permissions and log a warning as there may be an
    # issue with the backend provider.
    if not courses:
        logger.warning('Authorization server did not return course permissions. Defaulting to no course access.')
        courses = []
    else:
        courses = sorted(courses)

    set_user_course_permissions(user, courses)

    return courses


def get_user_course_permissions(user):
    """
    Return list of courses accessible by user.

    Arguments
        user (User) --  User for which course permissions should be returned
    """

    key_courses, key_last_updated = _get_course_permission_cache_keys(user)
    keys = [key_courses, key_last_updated]

    # Check the cache for data
    values = cache.get_many(keys)
    courses = values.get(key_courses, [])
    logger.error('getting cache {} {}'.format(user, len(courses)))

    # If data is not in the cache, refresh the permissions and validate against the new data.
    if not values.get(key_last_updated):
        courses = refresh_user_course_permissions(user)

    return courses


def user_can_view_course(user, course_id):
    """
    Returns boolean indicating if specified user can view specified course.

    Arguments
        user (User)     --  User whose permissions are being checked
        course_id (str) --  Course to check
    """
    courses = get_user_course_permissions(user)

    return course_id in courses
