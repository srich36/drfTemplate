from cross_copy_backend.settings.base import *

SECRET_KEY = 'abc123'

PRODUCTION = False
DEBUG = True
REDIRECT_403 = True


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

SESSION_COOKIE_AGE = 864000  # 10 days
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_SECURE = False  # There is no HTTPS locally, so the cookie will never be set if this is true
CSRF_COOKIE_SECURE = False

REDIS_HOST = config.get('REDIS', 'host', fallback='')
REDIS_DB = config.get('REDIS', 'db', fallback='1')

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://{}:6379/{}".format(REDIS_HOST, REDIS_DB),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}