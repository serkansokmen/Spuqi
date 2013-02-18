from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from qnotes.apps.topics.views import TopicList, TopicDetail, TopicCreate, TopicUpdate, TopicDelete

urlpatterns = patterns('',

    url(r'^$', login_required(TopicList.as_view()), name='topic_list'),
    url(r'^new/$', login_required(TopicCreate.as_view()), name='topic_add'),
    url(r'^(?P<slug>[\d\w\_\-]+)/$', login_required(TopicDetail.as_view()), name='topic_detail'),
    url(r'^(?P<slug>[\d\w\_\-]+)/edit/$', login_required(TopicUpdate.as_view()), name='topic_edit'),
    url(r'^(?P<slug>[\d\w\_\-]+)/delete/$', login_required(TopicDelete.as_view()), name='topic_delete'),

)
