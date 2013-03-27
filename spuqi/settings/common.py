#encoding:utf-8
'''Common settings and globals.'''

from os import environ
from datetime import timedelta
from os.path import abspath, basename, dirname, join, normpath
from sys import path
from djcelery import setup_loader


gettext = lambda s: s


ALLOWED_HOSTS = ['spuqi.herokuapp.com', 'www.spuqi.com', 'www.spuqy.com']


########## API-KEY CONFIGURATION
DISQUS_API_KEY = environ.get('SPUQI_DISQUS_API_KEY', '')
RECAPTCHA_PUBLIC_KEY = environ.get('SPUQI_RECAPTCHA_PUBLIC_KEY', '')
RECAPTCHA_PRIVATE_KEY = environ.get('SPUQI_RECAPTCHA_PRIVATE_KEY', '')
TWITTER_CONSUMER_KEY = environ.get('SPUQI_TWITTER_CONSUMER_KEY', '')
TWITTER_CONSUMER_SECRET = environ.get('SPUQI_TWITTER_CONSUMER_SECRET', '')
FACEBOOK_APP_ID = environ.get('SPUQI_FACEBOOK_APP_ID', '')
FACEBOOK_API_SECRET = environ.get('SPUQI_FACEBOOK_API_SECRET', '')
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

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Serkan Sökmen', 'spuqi.dev@gmail.com'),
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
    'spuqi.context_processors.site_processor',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
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
    'spuqi.middleware.ForceLangMiddleware',
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
    'imperavi',
    # django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    # django-avatar
    # 'avatar',
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
    # django-recaptcha
    'captcha',
    # django-restframework
    'rest_framework',
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
DISQUS_WEBSITE_SHORTNAME = 'spuqi'
########## END DISQUS CONFIGURATION


########## reCAPCTHA CONFIGURATION
RECAPTCHA_USE_SSL = True
########## END reCAPCTHA CONFIGURATION


########## AUTHENTICATION CONFIGURATION
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/'
LOGOUT_URL = '/accounts/logout/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

''' Don't use for now! '''
AUTH_USER_MODEL = 'accounts.SiteUser'
########## END AUTHENTICATION CONFIGURATION


########## ALLAUTH CONFIGURATION
# ACCOUNT_ADAPTER =
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_MIN_LENGTH = 6
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
ACCOUNT_PASSWORD_MIN_LENGTH = 6
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_AVATAR_SUPPORT = False
########## END ALLAUTH CONFIGURATION


########## REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    },
    'FILTER_BACKEND': 'rest_framework.filters.DjangoFilterBackend',
    'PAGINATE_BY': 10
}
########## END REST FRAMEWORK CONFIGURATION


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
GRAPPELLI_ADMIN_TITLE = u'Spuqi'
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
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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
