# coding=utf-8

import os
from django.utils.translation import ugettext_lazy

from oscar.defaults import *

DEBUG = True
DEBUG_TOOLBAR = True

ADMINS = (
    ('GabLeRoux', 'lebreton.gabriel@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

PROJECT_PATH = os.path.normpath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TIME_ZONE = 'America/Montreal'

SECRET_KEY = 'f&amp;qqn^!buj-m7*g0g1za8-+g3u+le9hpmktng(yp*1^-z+'

TEMPLATE_DEBUG = DEBUG

MANAGERS = ADMINS

# defines the site id (in database's sites)
if DEBUG:
    SITE_ID = 1
else:
    SITE_ID = 2

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en', ugettext_lazy(u'English')),
    ('fr', ugettext_lazy(u'Français')),
)

LANGUAGE_CODE = 'fr'

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, '../conf/locale'),
)

LOCALE_INDEPENDENT_PATHS = (
    r'^/admin/',
    r'^/localeurl/',
    r'^/api/',
    r'^/p/',
)

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

LOCALEURL_USE_ACCEPT_LANGUAGE = True

STATIC_ROOT = os.path.join(PROJECT_PATH, '../static')
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, '../local_static/'),
)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

# Now using jinja2 for template loader
TEMPLATE_LOADERS = (
    # 'django.template.loaders.filesystem.Loader',
    # 'django.template.loaders.app_directories.Loader',
    'django_jinja.loaders.AppLoader',
    'django_jinja.loaders.FileSystemLoader',
)

DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja2'

# JINJA2_ENVIRONMENT_OPTIONS = {
#     'block_start_string': '\BLOCK{',
#     'block_end_string': '}',
#     'variable_start_string': '\VAR{',
#     'variable_end_string': '}',
#     'comment_start_string': '\#{',
#     'comment_end_string': '}',
#     'line_statement_prefix': '%-',
#     'line_comment_prefix': '%#',
#     'trim_blocks': True,
#     'autoescape': False,
# }

MIDDLEWARE_CLASSES = (
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #userena
    'userena.middleware.UserenaLocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
)

ROOT_URLCONF = 'probe_app.urls'

from oscar import OSCAR_MAIN_TEMPLATE_DIR

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, '../templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    OSCAR_MAIN_TEMPLATE_DIR,
)

from oscar import get_core_apps

INSTALLED_APPS = [
                     'django_jinja',
                     'django_jinja.contrib._humanize',
                     'django_jinja.contrib._easy_thumbnails',
                     'django_jinja.contrib._pipeline',
                     'djangocms_admin_style',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.sites',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                     'django.contrib.admin',
                     'django.contrib.admindocs',
                     'probe_dispatcher',
                     'south',
                     'orderedmodel',
                     'custom_filters',
                     'localeurl',
                     'social_auth',
                     'rest_framework',
                     'compressor',

                     # userena
                     'userena',
                     'guardian',
                     'easy_thumbnails',
                     'accounts',
                 ] + get_core_apps()

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.Emailbackend',

    #userena
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',

    #django contrib
    'django.contrib.auth.backends.ModelBackend',
)

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.ProbeUserProfile'

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'probetestprobe@gmail.com'
EMAIL_HOST_PASSWORD = 'rYsMfnzwf7cReWift>darpQ4'

# debug_panel optional cache config
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     },
#
#     # this cache backend will be used by django-debug-panel
#     'debug-panel': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/debug-panel-cache',
#         'OPTIONS': {
#             'MAX_ENTRIES': 200
#         }
#     }
# }


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except:
    pass

if DEBUG and DEBUG_TOOLBAR:
    # debug_toolbar
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'debug_panel.middleware.DebugPanelMiddleware',
    )

    INSTALLED_APPS += [
        'debug_toolbar',
        'debug_panel',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': True,
    }