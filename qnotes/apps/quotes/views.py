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
        context['private_quotes'] = Quote.objects.filter(user=self.request.user, privacy_state=Quote.PRIVACY_STATES[2][0])
        context['active_tab'] = 'quotes'
        return context


class ReturnToQuoteDetailMixin(object):

    def get_success_url(self):
        return reverse('userena_profile_detail', kwargs={'username': self.request.user.username})


class QuoteList(QuotesMixin, ListView):
    context_object_name = 'quotes'

    def get_queryset(self):
        # return Quote.objects.filter(user=self.request.user)
        return Quote.objects.exclude(privacy_state=Quote.PRIVACY_STATES[2][0])


class QuoteDetail(QuotesMixin, DetailView):
    context_object_name = 'quote'

    def get_object(self):
        try:
            quote = Quote.objects.get(slug=self.kwargs['slug'])
            if quote.user == self.request.user:
                return quote
        except Quote.DoesNotExist:
            raise Http404
        return get_object_or_404(Quote, slug=self.kwargs['slug'], privacy_state=Quote.PRIVACY_STATES[2])


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
        return get_object_or_404(Quote, user=self.request.user, slug=self.kwargs['slug'])


class QuoteDelete(DeleteView):
    success_url = reverse_lazy('quote_list')

    def get_object(self):
        return get_object_or_404(Quote, user=self.request.user, slug=self.kwargs['slug'])
