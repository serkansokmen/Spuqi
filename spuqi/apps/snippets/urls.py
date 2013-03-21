from django.conf.urls import patterns, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns(
    'apps.snippets.views',
    url(r'^$', 'api_root'),
    url(r'^users/$', views.UserList.as_view(), name='siteuser-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='siteuser-detail'),
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
