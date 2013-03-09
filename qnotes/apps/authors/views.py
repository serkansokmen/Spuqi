from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from qnotes.apps.sources.models import Source
from .models import Author
from .forms import AuthorForm
from apps.helpers.views import FormNextMixin


class AuthorsMixin(object):

    def get_context_data(self, **kwargs):
        context = super(AuthorsMixin, self).get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['active_tab'] = 'authors'
        return context


class AuthorList(AuthorsMixin, ListView):
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.filter(user=self.request.user)


class AuthorDetail(AuthorsMixin, DetailView):
    context_object_name = 'current_author'

    def get_object(self):
        return get_object_or_404(Author, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        author = Author.objects.get(slug=self.kwargs['slug'])
        context['sources'] = Source.objects.filter(authors=author)
        return context


class AuthorCreate(AuthorsMixin, FormNextMixin, CreateView):
    model = Author
    form_class = AuthorForm
    success_url = 'author_list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AuthorCreate, self).form_valid(form)


class AuthorUpdate(AuthorsMixin, FormNextMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = 'author_list'

    def get_object(self):
        return get_object_or_404(Author, user=self.request.user, slug=self.kwargs['slug'])


class AuthorDelete(AuthorsMixin, FormNextMixin, DeleteView):
    success_url = 'author_list'

    def get_object(self):
        return get_object_or_404(Author, user=self.request.user, slug=self.kwargs['slug'])
