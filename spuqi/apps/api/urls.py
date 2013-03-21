from django.conf.urls import patterns, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns(
    'apps.api.views',
    (r'^$', 'api_root'),
    url(r'^users/$', views.UserList.as_view(), name='siteuser-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='siteuser-detail'),
    url(r'^authors/$', views.AuthorList.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetail.as_view(), name='author-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
