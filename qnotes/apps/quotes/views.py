from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.forms import ValidationError
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from qnotes.apps.quotes.models import Quote
from qnotes.apps.quotes.forms import QuoteForm


class QuoteList(ListView):
    context_object_name = 'quotes'

    def get_context_data(self, **kwargs):
        context = super(QuoteList, self).get_context_data(**kwargs)
        context['private_quotes'] = Quote.objects.filter(user=self.request.user, is_private=True)
        return context

    def get_queryset(self):
        # return Quote.objects.filter(user=self.request.user)
        return Quote.objects.filter(is_private=False)


class QuoteDetail(DetailView):
    context_object_name = 'current_quote'

    def get_object(self):
        try:
            quote = Quote.objects.get(user=self.request.user, pk=self.kwargs['pk'])
            if quote.user == self.request.user:
                return quote
        except Quote.DoesNotExist:
            raise Http404
        return get_object_or_404(Quote, user=self.request.user, pk=self.kwargs['pk'], is_private=False)


class QuoteCreate(CreateView):
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


class QuoteUpdate(UpdateView):
    model = Quote
    form_class = QuoteForm

    def get_object(self):
        return get_object_or_404(Quote, user=self.request.user, pk=self.kwargs['pk'])


class QuoteDelete(DeleteView):
    success_url = reverse_lazy('quote_list')

    def get_object(self):
        return get_object_or_404(Quote, user=self.request.user, pk=self.kwargs['pk'])
