from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from qnotes.apps.authors.models import Author
from qnotes.apps.sources.models import Source
from qnotes.apps.authors.forms import AuthorForm


class AuthorSidebarMixin(object):
    # Add collections to the context
    def get_context_data(self, **kwargs):
        context = super(AuthorSidebarMixin, self).get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['active_tab'] = 'authors'
        return context


class AuthorList(AuthorSidebarMixin, ListView):
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.filter(user=self.request.user)


class AuthorDetail(AuthorSidebarMixin, DetailView):
    context_object_name = 'current_author'

    def get_object(self):
        return get_object_or_404(Author, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        author = Author.objects.get(slug=self.kwargs['slug'])
        context['sources'] = Source.objects.filter(authors=author)
        return context


class AuthorCreate(AuthorSidebarMixin, CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AuthorCreate, self).form_valid(form)


class AuthorUpdate(AuthorSidebarMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')

    def get_object(self):
        return get_object_or_404(Author, user=self.request.user, slug=self.kwargs['slug'])


class AuthorDelete(AuthorSidebarMixin, DeleteView):
    success_url = reverse_lazy('author_list')

    def get_object(self):
        return get_object_or_404(Author, user=self.request.user, slug=self.kwargs['slug'])
