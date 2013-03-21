from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
# from apps.accounts.forms import SignupFormReCaptcha, SigninFormReCaptcha

from django.db.models.loading import cache as model_cache
if not model_cache.loaded:
    model_cache.get_models()

admin.autodiscover()

urlpatterns = patterns(
    '',

    (r'', include('social_auth.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),

    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^survey/$', TemplateView.as_view(template_name='survey.html'), name='survey'),

    # (r'^admin/', include('smuggler.urls')),  # put it before admin url patterns
    url(r'^admin/', include(admin.site.urls)),

    # local apps
    (r'^authors/', include('apps.authors.urls')),
    (r'^collections/', include('apps.collections.urls')),
    (r'^quotes/', include('apps.quotes.urls')),
    (r'^sources/', include('apps.sources.urls')),

    # api urls
    url(r'^api/', include('apps.api.urls')),
    # django-restframework default login/logout views
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # django-grappelli
    (r'^grappelli/', include('grappelli.urls')),


    # (r'^robots\.txt$', 'django.views.generic.simple.direct_to_template', {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    # (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'})
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
