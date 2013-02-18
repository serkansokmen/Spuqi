from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from qnotes.apps.authors.views import AuthorList, AuthorDetail, AuthorCreate, AuthorUpdate, AuthorDelete

urlpatterns = patterns('',

    url(r'^$', login_required(AuthorList.as_view()), name='author_list'),
    url(r'^new/$', login_required(AuthorCreate.as_view()), name='author_add'),
    url(r'^(?P<slug>[\d\w\_\-]+)/$', login_required(AuthorDetail.as_view()), name='author_detail'),
    url(r'^(?P<slug>[\d\w\_\-]+)/edit/$', login_required(AuthorUpdate.as_view()), name='author_edit'),
    url(r'^(?P<slug>[\d\w\_\-]+)/delete/$', login_required(AuthorDelete.as_view()), name='author_delete'),

)
