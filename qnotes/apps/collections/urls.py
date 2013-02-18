from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from qnotes.apps.collections.views import CollectionList, CollectionDetail, CollectionCreate, CollectionUpdate, CollectionDelete

urlpatterns = patterns('',

    url(r'^$', login_required(CollectionList.as_view()), name='collection_list'),
    url(r'^new/$', login_required(CollectionCreate.as_view()), name='collection_add'),
    url(r'^(?P<slug>[\d\w\_\-]+)/$', login_required(CollectionDetail.as_view()), name='collection_detail'),
    url(r'^(?P<slug>[\d\w\_\-]+)/edit/$', login_required(CollectionUpdate.as_view()), name='collection_edit'),
    url(r'^(?P<slug>[\d\w\_\-]+)/delete/$', login_required(CollectionDelete.as_view()), name='collection_delete'),

)
