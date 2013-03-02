from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import redirect_to

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^$', redirect_to, {'url': 'quote/'}),

    # django-grappelli
    (r'^grappelli/', include('grappelli.urls')),
    # (r'^admin/', include('smuggler.urls')),  # put it before admin url patterns
    (r'^admin/', include(admin.site.urls)),

    # django-userena URLs
    (r'^accounts/', include('userena.urls')),

    # local app URLs
    (r'^author/', include('apps.authors.urls')),
    (r'^collection/', include('apps.collections.urls')),
    (r'^quote/', include('apps.quotes.urls')),
    (r'^source/', include('apps.sources.urls')),
    (r'^topic/', include('apps.topics.urls')),

    # django-select2 URLs
    (r'^ext/', include('django_select2.urls')),
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
