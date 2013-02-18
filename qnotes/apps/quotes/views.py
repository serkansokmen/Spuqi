from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.forms import ValidationError
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from qnotes.apps.quotes.models import Quote
from qnotes.apps.quotes.forms import QuoteForm


@login_required
def profile(request):
    return HttpResponseRedirect(reverse('quotes'))


class QuoteSidebarMixin(object):
    # Add collections to the context
    def get_context_data(self, **kwargs):
        context = super(QuoteSidebarMixin, self).get_context_data(**kwargs)
        # context['quotes'] = Quote.objects.filter(user=self.request.user)
        context['quotes'] = Quote.objects.all()
        context['active_tab'] = 'quotes'
        return context


class QuoteList(QuoteSidebarMixin, ListView):
    context_object_name = 'quotes'

    def get_queryset(self):
        # return Quote.objects.filter(user=self.request.user)
        return Quote.objects.all()


class QuoteDetail(QuoteSidebarMixin, DetailView):
    context_object_name = 'current_quote'

    def get_object(self):
        # return get_object_or_404(Quote, user=self.request.user, pk=self.kwargs['pk'])
        return get_object_or_404(Quote, pk=self.kwargs['pk'])


class QuoteCreate(QuoteSidebarMixin, CreateView):
    model = Quote
    form_class = QuoteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        """ if the user is supplied, check if the user has a blog item
            with the same slug at the same day
        """
        if self.request.user and not form.errors and not form.instance.id:
            try:
                quote = Quote.objects.get(quote=form.cleaned_data['quote'],
                                        user=self.request.user)
            except Quote.DoesNotExist:
                pass
            else:
                msg = mark_safe('%s: %s' %
                                (_('You have already created this quote'),
                                quote.quote))
                raise ValidationError(msg)
        return super(QuoteCreate, self).form_valid(form)


class QuoteUpdate(QuoteSidebarMixin, UpdateView):
    model = Quote
    form_class = QuoteForm

    def get_object(self):
        return get_object_or_404(Quote, user=self.request.user, pk=self.kwargs['pk'])


class QuoteDelete(QuoteSidebarMixin, DeleteView):
    success_url = reverse_lazy('quote_list')

    def get_object(self):
        return get_object_or_404(Quote, user=self.request.user, pk=self.kwargs['pk'])
