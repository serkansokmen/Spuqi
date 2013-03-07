from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from qnotes.apps.quotes.models import Quote
from qnotes.apps.authors.views import AuthorFormMixin
from .models import Source
from .forms import SourceForm
from endless_pagination.views import AjaxListView


class SourceList(AjaxListView):
    context_object_name = 'sources'

    def get_queryset(self):
        return Source.objects.filter(user=self.request.user)


class SourceDetail(DetailView):
    context_object_name = 'current_source'

    def get_object(self):
        return get_object_or_404(Source, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(SourceDetail, self).get_context_data(**kwargs)
        source = get_object_or_404(Source, slug=self.kwargs['slug'])
        context['source_quotes'] = Quote.objects.filter(source=source)
        return context


class SourceFormWithNextMixin(object):

    def get_success_url(self):
        if self.request.GET['next']:
            return self.request.GET['next']
        return reverse_lazy('source_list')


class SourceCreate(AuthorFormMixin, SourceFormWithNextMixin, CreateView):
    model = Source
    form_class = SourceForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SourceCreate, self).form_valid(form)


class SourceUpdate(AuthorFormMixin, SourceFormWithNextMixin, UpdateView):
    model = Source
    form_class = SourceForm

    def get_object(self):
        return get_object_or_404(Source, user=self.request.user, slug=self.kwargs['slug'])


class SourceDelete(DeleteView):
    success_url = reverse_lazy('source_list')

    def get_object(self):
        return get_object_or_404(Source, user=self.request.user, slug=self.kwargs['slug'])
