from django.conf.urls import patterns, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns(
    '',
    (r'^$', 'apps.api.views.api_root'),
    url(r'^users/$',
        views.UserList.as_view(), name='siteuser-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(), name='siteuser-detail'),
    url(r'^authors/$',
        views.AuthorList.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>[0-9]+)/$',
        views.AuthorDetail.as_view(), name='author-detail'),
    url(r'^sources/$',
        views.SourceList.as_view(), name='source-list'),
    url(r'^sources/(?P<pk>[0-9]+)/$',
        views.SourceDetail.as_view(), name='source-detail'),
    url(r'^collections/$',
        views.CollectionList.as_view(), name='collection-list'),
    url(r'^collections/(?P<pk>[0-9]+)/$',
        views.CollectionDetail.as_view(), name='collection-detail'),
    url(r'^quotes/$',
        views.QuoteList.as_view(), name='quote-list'),
    url(r'^quotes/(?P<pk>[0-9]+)/$',
        views.QuoteDetail.as_view(), name='quote-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
