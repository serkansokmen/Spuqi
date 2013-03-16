#encoding:utf-8
'''Common settings and globals.'''

from os import environ
from datetime import timedelta
from os.path import abspath, basename, dirname, join, normpath
from sys import path
from djcelery import setup_loader


gettext = lambda s: s


ALLOWED_HOSTS = ['qnotes.herokuapp.com', ]


########## API-KEY CONFIGURATION
DISQUS_API_KEY = environ.get('QNOTES_DISQUS_API_KEY', '')
RECAPTCHA_PUBLIC_KEY = environ.get('QNOTES_RECAPTCHA_PUBLIC_KEY', '')
RECAPTCHA_PRIVATE_KEY = environ.get('QNOTES_RECAPTCHA_PRIVATE_KEY', '')
TWITTER_CONSUMER_KEY = environ.get('QNOTES_TWITTER_CONSUMER_KEY', '')
TWITTER_CONSUMER_SECRET = environ.get('QNOTES_TWITTER_CONSUMER_SECRET', '')
FACEBOOK_APP_ID = environ.get('QNOTES_FACEBOOK_APP_ID', '')
FACEBOOK_APP_SECRET = environ.get('QNOTES_FACEBOOK_APP_SECRET', '')
########## END API-KEY CONFIGURATION

########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
SOUTH_TESTS_MIGRATE = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Serkan Sökmen', 'quotesnotesapp@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Europe/Istanbul'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'tr'

LANGUAGES = (
    ('en', gettext('English')),
    ('tr', gettext('Turkish')),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = False
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'assets')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    'dajaxice.finders.DajaxiceFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = 'donttellanyone'
########## END SECRET CONFIGURATION


########## ROSETTA CONFIGURATION
ROSETTA_STORAGE_CLASS = 'rosetta.storage.CacheRosettaStorage'
########## END ROSETTA CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(DJANGO_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'qnotes.context_processors.site_processor',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Use GZip compression to reduce bandwidth.
    'django.middleware.gzip.GZipMiddleware',

    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'qnotes.middleware.ForceLangMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Useful template tags:
    'django.contrib.humanize',
    # django-grappelli
    'grappelli',
    # Admin panel and documentation:
    'django.contrib.admin',
    'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    # Database migration helpers:
    'south',
    # Compressor:
    'compressor',
    # Asynchronous task queue:
    'djcelery',
    # Rosetta
    'rosetta',
    # django-social-auth
    'social_auth',
    # django-extra-views
    'extra_views',
    # django-taggit
    'taggit',
    # django-endless-pagination
    'endless_pagination',
    # easy_thumbnails
    'easy_thumbnails',
    # django-bootstrap-form
    'bootstrapform',
    # django-disqus
    'disqus',
    # django-dajaxice
    'dajaxice',
    # django-recaptcha
    'captcha',
)

LOCAL_APPS = (
    # Profile
    'apps.accounts',
    # Quotes application
    'apps.collections',
    'apps.sources',
    'apps.authors',
    'apps.quotes',
    'apps.helpers',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## SMUGGLER CONFIGURATION
SMUGGLER_EXCLUDE_LIST = []  # 'app_label.ModelName'
SMUGGLER_FIXTURE_DIR = 'fixtures/'
SMUGGLER_FORMAT = 'json'
SMUGGLER_INDENT = 2
########## END SMUGGLER CONFIGURATION


########## EASY THUMBNAILS CONFIGURATION
THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (31, 31), 'crop': 'smart'},
        'avatar_small': {'size': (21, 21), 'crop': 'smart'},
        'avatar_large': {'size': (64, 64), 'crop': 'smart'},
    },
}
########## END EASY THUMBNAILS CONFIGURATION


########## DISQUS CONFIGURATION
DISQUS_WEBSITE_SHORTNAME = 'qnotes'
########## END DISQUS CONFIGURATION


########## reCAPCTHA CONFIGURATION
RECAPTCHA_USE_SSL = True
########## END reCAPCTHA CONFIGURATION


########## AUTHENTICATION CONFIGURATION
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/quotes/'
LOGIN_ERROR_URL = '/'
LOGOUT_URL = '/logout/'

AUTH_USER_MODEL = 'accounts.SiteUser'

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    # 'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)
########## END AUTHENTICATION CONFIGURATION


########## SOCIAL AUTH CONFIGURATION
SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL
SOCIAL_AUTH_CREATE_USERS = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
import random
SOCIAL_AUTH_DEFAULT_USERNAME = lambda: random.choice(['Darth Vader', 'Obi-Wan Kenobi', 'R2-D2', 'C-3PO', 'Yoda'])
SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
# SOCIAL_AUTH_ASSOCIATE_BY_MAIL = True

FACEBOOK_EXTENDED_PERMISSIONS = ['email']
FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'display': 'touch'}
FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'tr_TR'}
########## END SOCIAL AUTH CONFIGURATION


########## AJAX SELECTS CONFIGURATION
# define the lookup channels in use on the site
AJAX_LOOKUP_CHANNELS = {
    # pass a dict with the model and the field to search against
    'authors': {'model': 'authors.Author', 'search_field': 'name'},
}
# magically include jqueryUI/js/css
AJAX_SELECT_BOOTSTRAP = True
AJAX_SELECT_INLINES = 'inline'
########## END AJAX SELECTS CONFIGURATION


########## GRAPPELLI CONFIGURATION
GRAPPELLI_ADMIN_TITLE = u'Qnotes'
AUTOCOMPLETE_LIMIT = 10
########## END GRAPPELLI CONFIGURATION


########## CELERY CONFIGURATION
# See: http://celery.readthedocs.org/en/latest/configuration.html#celery-task-result-expires
CELERY_TASK_RESULT_EXPIRES = timedelta(minutes=30)
# See: http://celery.github.com/celery/django/
setup_loader()
########## END CELERY CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'
########## END WSGI CONFIGURATION


########## COMPRESSION CONFIGURATION
# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_ENABLED
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
)

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS
COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]
########## END COMPRESSION CONFIGURATION


########## DJANGO ENDLESS PAGINATION CONFIGURATION
ENDLESS_PAGINATION_PER_PAGE = 5
ENDLESS_PAGINATION_PAGE_LABEL = 'p'
ENDLESS_PAGINATION_LOADING = '<i class="icon-spinner icon-large icon-spin"></i>'
########## END DJANGO ENDLESS PAGINATION CONFIGURATION

########## OTHER CONFIGURATION
FIRST_DAY_OF_WEEK = 1


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': [],
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
########## END LOGGING CONFIGURATION
