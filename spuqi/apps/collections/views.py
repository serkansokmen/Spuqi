from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Collection
from .forms import CollectionForm
from apps.helpers.views import FormNextMixin


class CollectionMixin(object):
    # Add collections to the context
    def get_context_data(self, **kwargs):
        context = super(CollectionMixin, self).get_context_data(**kwargs)
        context['owned_collections'] = Collection.objects.filter(user=self.request.user)
        # context['followed_collections'] = Collection.objects.filter(members=self.request.user).exclude(user=self.request.user)
        context['active_tab'] = 'collections'
        return context


class CollectionList(CollectionMixin, ListView):
    model = Collection
    context_object_name = 'collections'


class CollectionDetail(CollectionMixin, DetailView):
    model = Collection
    context_object_name = 'current_collection'

    def get_context_data(self, **kwargs):
        context = super(CollectionDetail, self).get_context_data(**kwargs)
        collection = Collection.objects.get(slug=self.kwargs['slug'])
        context['collection_sources'] = collection.sources.all()
        return context


class CollectionCreate(CollectionMixin, FormNextMixin, CreateView):
    model = Collection
    form_class = CollectionForm
    success_url = 'collection_list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CollectionCreate, self).form_valid(form)


class CollectionUpdate(CollectionMixin, FormNextMixin, UpdateView):
    model = Collection
    form_class = CollectionForm
    slug_field = 'slug'
    success_url = 'collection_list'


class CollectionDelete(CollectionMixin, FormNextMixin, DeleteView):
    success_url = 'collection_list'

    def get_object(self):
        return get_object_or_404(Collection, user=self.request.user, slug=self.kwargs['slug'])
