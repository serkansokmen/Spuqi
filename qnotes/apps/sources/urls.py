from django.conf.urls import *
from django.contrib.auth.decorators import login_required
from qnotes.apps.sources.views import SourceList, SourceDetail, SourceCreate, SourceUpdate, SourceDelete

urlpatterns = patterns('',

    url(r'^$', login_required(SourceList.as_view()), name='source_list'),
    url(r'^new/$', login_required(SourceCreate.as_view()), name='source_add'),
    url(r'^(?P<slug>[\d\w\_\-]+)/$', login_required(SourceDetail.as_view()), name='source_detail'),
    url(r'^(?P<slug>[\d\w\_\-]+)/edit/$', login_required(SourceUpdate.as_view()), name='source_edit'),
    url(r'^(?P<slug>[\d\w\_\-]+)/delete/$', login_required(SourceDelete.as_view()), name='source_delete'),

)
