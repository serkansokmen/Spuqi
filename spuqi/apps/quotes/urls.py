from django.conf.urls import *
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import (
    QuoteList, QuoteDetail, QuoteCreate, QuoteUpdate, QuoteDelete
)

urlpatterns = patterns(
    '',
    url(r'^$', login_required(QuoteList.as_view()), name='quote_list'),
    url(r'^new/$', login_required(QuoteCreate.as_view()), name='quote_add'),
    url(r'^app/$', TemplateView.as_view(template_name='quotes/app.html'), name='quotes_app'),
    url(r'^(?P<slug>[\d\w\_\-]+)/$', login_required(QuoteDetail.as_view()), name='quote_detail'),
    url(r'^(?P<slug>[\d\w\_\-]+)/edit/$', login_required(QuoteUpdate.as_view()), name='quote_edit'),
    url(r'^(?P<slug>[\d\w\_\-]+)/delete/$', login_required(QuoteDelete.as_view()), name='quote_delete'),
)
