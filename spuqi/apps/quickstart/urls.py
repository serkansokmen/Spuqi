from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.quickstart import views


urlpatterns = patterns(
    'apps.quickstart.views',
    url(r'^$', 'api_root'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^groups/$', views.GroupList.as_view(), name='group-list'),
    url(r'^groups/(?P<pk>\d+)/$', views.GroupDetail.as_view(), name='group-detail'),
)


# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])


# Default login/logout views
urlpatterns += patterns(
    '',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
