# coding=utf-8
"""Base settings shared by all environments"""

import os

# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *

import probe_project as project_module

# noinspection PyUnresolvedReferences
from django.utils.translation import ugettext_lazy as _

from oscar import OSCAR_MAIN_TEMPLATE_DIR

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'f&amp;qqn^!buj-m7*g0g1za8-+g3u+le9hpmktng(yp*1^-z+'

# in database, 1 points to localhost:8000, 2 points to webprobe.io
# redefined in production.py
SITE_ID = 1

ADMINS = (
    ('GabLeRoux', 'lebreton.gabriel@gmail.com'),
    ('nsb002', 'nsb002@gmail.com'),
    ('kimlavoie14', 'kim.lavoie.14@gmail.com'),
)

MANAGERS = ADMINS

INSTALLED_APPS = (
    'probe_project.apps.accounts',
    'probe_project.apps.probe_dispatcher',
    # 'probe_project.apps.orderedmodel',

    'south',
    'django_extensions',

    'userena',
    'guardian',
    # 'easy_thumbnails',

    # social auth
    'social.apps.django_app.default',


    'menu',

    'localeurl',
    'rest_framework',
    'compressor',

    'oscar',
    'haystack',

    'bootstrapform',

    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))

# PYTHON_BIN = os.path.dirname(sys.executable)

#==============================================================================
# Project URLS auth and media settings
#==============================================================================

ROOT_URLCONF = 'probe_project.urls'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')   
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'local_static'),
)

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'uploads')

ADMIN_MEDIA_PREFIX = '/static/admin/'

ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.ProbeUserProfile'

LOGIN_REDIRECT_URL = '/dashboard/'
LOGIN_URL = '/signin/'
LOGOUT_URL = '/signout/'

#==============================================================================
# Templates
#==============================================================================

# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
    OSCAR_MAIN_TEMPLATE_DIR,
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',

    'django.core.context_processors.request',

    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
)

#==============================================================================
# i18n and l10n
#==============================================================================

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/Montreal'

USE_TZ = True
USE_I18N = True
USE_L10N = True

LANGUAGES = (
    ('en', _(u'English')),
    ('fr', _(u'Français')),
)

LANGUAGE_CODE = 'fr'

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, 'conf/locale'),
)

LOCALE_INDEPENDENT_PATHS = (
    r'^/admin/',
    r'^/localeurl/',
    r'^/api/',
    r'^/p/',
    r'^/favicon.ico',
    r'^/social/',
)

LOCALE_INDEPENDENT_MEDIA_URL = True
LOCALE_INDEPENDENT_STATIC_URL = True
PREFIX_DEFAULT_LOCALE = True
LOCALEURL_USE_ACCEPT_LANGUAGE = True


#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (
    'oscar.apps.basket.middleware.BasketMiddleware',
    'localeurl.middleware.LocaleURLMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',

    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#==============================================================================
# Auth / security
#==============================================================================

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.Emailbackend',
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',

    "django.contrib.auth.backends.ModelBackend",

    'social.backends.github.GithubOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GooglePlusAuth',
)

# GOOGLE_OAUTH2_CLIENT_ID = '440027041129-hpcmjm5epmqr6bbm5kgobdd3fmps4ebt.apps.googleusercontent.com'
# GOOGLE_OAUTH2_CLIENT_SECRET = 'VfyRCLADLEN8gJbeFglCaPav'
#
# GITHUB_APP_ID = '89fbe87089436ea76f71'
# GITHUB_API_SECRET = '876ed85504747328c64895259adc0392a89c8e44'


# AUTH_USER_MODEL = 'app_label.model_name'

SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/userinfo.profile'
]
# # SOCIAL_AUTH_EMAIL_FORM_URL = '/signup-email'
# SOCIAL_AUTH_EMAIL_FORM_HTML = 'email_signup.html'
# SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'example.app.mail.send_validation'
# SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/email-sent/'
# # SOCIAL_AUTH_USERNAME_FORM_URL = '/signup-username'
# SOCIAL_AUTH_USERNAME_FORM_HTML = 'username_signup.html'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'probe_project.apps.accounts.pipeline.require_email',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

# SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['first_name', 'last_name', 'email',
#                                         'username']

#==============================================================================
# Third party app settings
#==============================================================================

# noinspection PyUnresolvedReferences
from oscar.defaults import *

INSTALLED_APPS += (
    'oscar',
    'oscar.apps.analytics',
    'oscar.apps.checkout',
    'oscar.apps.address',
    'oscar.apps.shipping',
    'oscar.apps.catalogue',
    'oscar.apps.catalogue.reviews',
    'oscar.apps.partner',
    'oscar.apps.basket',
    'oscar.apps.payment',
    'oscar.apps.offer',
    'oscar.apps.order',
    'oscar.apps.customer',
    'oscar.apps.promotions',
    'oscar.apps.search',
    'oscar.apps.voucher',
    'oscar.apps.wishlists',
    'oscar.apps.dashboard',
    'oscar.apps.dashboard.reports',
    'oscar.apps.dashboard.users',
    'oscar.apps.dashboard.orders',
    'oscar.apps.dashboard.promotions',
    'oscar.apps.dashboard.catalogue',
    'oscar.apps.dashboard.offers',
    'oscar.apps.dashboard.partners',
    'oscar.apps.dashboard.pages',
    'oscar.apps.dashboard.ranges',
    'oscar.apps.dashboard.reviews',
    'oscar.apps.dashboard.vouchers',
    'oscar.apps.dashboard.communications',
    # 3rd-party apps that oscar depends on
    'treebeard',
    'sorl.thumbnail',
    'django.contrib.flatpages',

)

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

#==============================================================================
# Email and logging
#==============================================================================

# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'probetestprobe@gmail.com'
EMAIL_HOST_PASSWORD = 'rYsMfnzwf7cReWift>darpQ4'


# Send an email to the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize logging configuration.
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
            'handlers': ['mail_admins'],  # sends a mail to admins on error!
            'level': 'ERROR',
            'propagate': True,
        },
    }
}