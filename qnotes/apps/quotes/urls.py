from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from qnotes.apps.quotes.views import (
    QuoteList, QuoteDetail, QuoteCreate, QuoteUpdate, QuoteDelete
)

urlpatterns = patterns(
    '',
    url(r'^$', login_required(QuoteList.as_view()), name='quote_list'),
    url(r'^new/$', login_required(QuoteCreate.as_view()), name='quote_add'),
    url(r'^(?P<pk>\d+)/$', login_required(QuoteDetail.as_view()), name='quote_detail'),
    url(r'^(?P<pk>\d+)/edit/$', login_required(QuoteUpdate.as_view()), name='quote_edit'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(QuoteDelete.as_view()), name='quote_delete'),
)
