from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from apps.accounts.forms import SignupFormReCaptcha, SigninFormReCaptcha
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    # (r'^admin/', include('smuggler.urls')),  # put it before admin url patterns
    (r'^admin/', include(admin.site.urls)),

    # django-userena
    (r'^accounts/signup/$', 'userena.views.signup', {'signup_form': SignupFormReCaptcha}),
    (r'^accounts/signin/$', 'userena.views.signin', {'auth_form': SigninFormReCaptcha}),
    (r'^accounts/', include('userena.urls')),

    # local apps
    (r'^authors/', include('apps.authors.urls')),
    (r'^collections/', include('apps.collections.urls')),
    (r'^quotes/', include('apps.quotes.urls')),
    (r'^sources/', include('apps.sources.urls')),

    # django-grappelli
    (r'^grappelli/', include('grappelli.urls')),

    # django-dajaxice
    (dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    (r'^robots\.txt$', 'django.views.generic.simple.direct_to_template', {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'})
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^404/$', 'django.views.defaults.page_not_found'),
        (r'^500/$', 'django.views.defaults.server_error'),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        (r'^rosetta/', include('rosetta.urls')),
    )

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns(
        '',
        url(r'^rosetta/', include('rosetta.urls')),
    )
