from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from qnotes.apps.quotes.models import Quote
from .models import Source
from .forms import SourceForm
from apps.helpers.views import FormNextMixin


class SourceList(ListView):
    context_object_name = 'sources'

    def get_queryset(self):
        return Source.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(SourceList, self).get_context_data(**kwargs)
        context['active_tab'] = 'sources'
        return context


class SourceDetail(DetailView):
    context_object_name = 'current_source'

    def get_object(self):
        return get_object_or_404(Source, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(SourceDetail, self).get_context_data(**kwargs)
        source = get_object_or_404(Source, slug=self.kwargs['slug'])
        context['active_tab'] = 'sources'
        context['source_quotes'] = Quote.objects.filter(source=source)
        return context


class SourceCreate(FormNextMixin, CreateView):
    model = Source
    form_class = SourceForm
    success_url = 'source_list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SourceCreate, self).form_valid(form)


class SourceUpdate(FormNextMixin, UpdateView):
    model = Source
    form_class = SourceForm
    success_url = 'source_list'

    def get_object(self):
        return get_object_or_404(Source, user=self.request.user, slug=self.kwargs['slug'])


class SourceDelete(FormNextMixin, DeleteView):
    success_url = 'source_list'

    def get_object(self):
        return get_object_or_404(Source, user=self.request.user, slug=self.kwargs['slug'])
