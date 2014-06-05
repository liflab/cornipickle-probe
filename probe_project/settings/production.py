"""
Settings for Production Server
"""
from probe_project.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SITE_ID = 2  # webprobe.io

VAR_ROOT = '/var/www/probe_project'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'probe_project',
        'USER': 'probe',
        'PASSWORD': 'R=jibiqeK9Xg2rBzmshxxtfW',
    }
}

# WSGI_APPLICATION = 'probe_project.wsgi.application'
