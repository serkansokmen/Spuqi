from django.http import Http404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
# from django.utils.translation import ugettext as _
from .models import Quote
from .forms import QuoteForm


class QuotesMixin(object):

    def get_context_data(self, **kwargs):
        context = super(QuotesMixin, self).get_context_data(**kwargs)
        context['private_quotes'] = Quote.objects.filter(user=self.request.user, is_private=True)
        return context


class ReturnToQuoteDetailMixin(object):

    def get_success_url(self):
        return reverse('userena_profile_detail', kwargs={'username': self.request.user.username})


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
    context_object_name = 'quote'

    def get_object(self):
        try:
            quote = Quote.objects.get(pk=self.kwargs['pk'])
            if quote.user == self.request.user:
                return quote
        except Quote.DoesNotExist:
            raise Http404
        return get_object_or_404(Quote, pk=self.kwargs['pk'], is_private=False)


class QuoteCreate(ReturnToQuoteDetailMixin, CreateView):
    model = Quote
    form_class = QuoteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        """ if the user is supplied, check if the user has a quote
            with the same slug at the same day
        """
        '''
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
        '''
        return super(QuoteCreate, self).form_valid(form)


class QuoteUpdate(ReturnToQuoteDetailMixin, UpdateView):
    model = Quote
    form_class = QuoteForm

    def get_object(self):
        return get_object_or_404(Quote, user=self.request.user, pk=self.kwargs['pk'])


class QuoteDelete(DeleteView):
    success_url = reverse_lazy('quote_list')

    def get_object(self):
        return get_object_or_404(Quote, user=self.request.user, pk=self.kwargs['pk'])
