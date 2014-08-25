"""
Django settings for noball_django project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# applicationの名前
APPLICATION_NAME = 'PyBall'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3+ug=l%6*!!3abr*+v&kk85slo^o3r-qkca+3^m%h)xme!0%8o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if not DEBUG:
    VIEW_ENCODE='en_US.utf8'
    ALLOWED_HOSTS=[
        '127.0.0.1',
        'localhost',
        's14',
        'noball.gehirn.ne.jp',
        'noball.shinyorke.info',
    ]
else:
    # VIEW_ENCODE='ja_JP.utf8'  # Debian
    VIEW_ENCODE='en_US'
    ALLOWED_HOSTS=[
        '127.0.0.1',
        'localhost',
    ]

TEMPLATE_DEBUG = True

TIME_ZONE = 'Asia/Tokyo'
LANGUAGE_CODE = 'ja'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mlb',
)

STATIC_ROOT = os.path.join(BASE_DIR, 'deploy')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'noball_django.urls'

WSGI_APPLICATION = 'noball_django.wsgi.application'


TEMPLATE_DIRS = (
    './templates'
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sean_lahman',                      # Or path to database file if using sqlite3.
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '192.168.33.10',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
