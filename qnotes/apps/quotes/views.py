from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.forms import ValidationError
from .models import Quote
from .forms import QuoteForm


class QuotesMixin(object):

    def get_context_data(self, **kwargs):
        context = super(QuotesMixin, self).get_context_data(**kwargs)
        context['active_tab'] = 'quotes'
        return context


class ReturnToQuoteDetailMixin(object):

    def get_success_url(self):
        return reverse('userena_profile_detail', kwargs={'username': self.request.user.username})


class QuoteList(QuotesMixin, ListView):
    context_object_name = 'quotes'
    template_name = 'quotes/quote_list_page.html'

    def get_queryset(self):
        wanted_quotes = set()
        # authenticated user's PRIVATE Quote objects
        if self.request.user.is_authenticated():
            for quote in Quote.objects.filter(
                user=self.request.user, privacy_state=Quote.PRIVATE
            ):
                wanted_quotes.add(quote.pk)
        # OPEN and READ_ONLY Quote objects
        for quote in Quote.objects.exclude(privacy_state=Quote.PRIVATE):
            wanted_quotes.add(quote.pk)

        # exclude private quotes
        return Quote.objects.filter(id__in=wanted_quotes)


class QuoteDetail(QuotesMixin, DetailView):
    context_object_name = 'quote'

    def get_object(self):
        # try to get Quote object
        quote = get_object_or_404(
            Quote,
            slug=self.kwargs['slug'],
        )
        # if quote is private
        if quote.privacy_state == Quote.PRIVATE:
            # if user owns quote or it is someone else, return forbidden
            return quote if quote.user == self.request.user else HttpResponseForbidden()
        # or else return Quote object
        else:
            return quote


class QuoteCreate(ReturnToQuoteDetailMixin, CreateView):
    model = Quote
    form_class = QuoteForm

    def form_valid(self, form):
        # set instance user
        form.instance.user = self.request.user
        # if the quote and source is supplied, check if there is another
        # quote with the same source
        if self.request.user and not form.errors and not form.instance.id:
            if Quote.objects.filter(
                quote=form.instance.quote,
                source=form.instance.source
            ).count() > 0:
                msg = mark_safe(
                    '%s' % _('This quotation is already created.')
                )
                raise ValidationError(msg)
        return super(QuoteCreate, self).form_valid(form)


class QuoteUpdate(ReturnToQuoteDetailMixin, UpdateView):
    model = Quote
    form_class = QuoteForm

    def get_object(self):
        return get_object_or_404(Quote, user=self.request.user, slug=self.kwargs['slug'])


class QuoteDelete(DeleteView):
    success_url = reverse_lazy('quote_list')

    def get_object(self):
        return get_object_or_404(Quote, user=self.request.user, slug=self.kwargs['slug'])
