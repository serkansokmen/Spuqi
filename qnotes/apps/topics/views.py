from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from qnotes.apps.topics.models import Topic
from qnotes.apps.quotes.models import Quote
from qnotes.apps.topics.forms import TopicForm


class TopicSidebarMixin(object):
    # Add collections to the context
    def get_context_data(self, **kwargs):
        context = super(TopicSidebarMixin, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        context['active_tab'] = 'topics'
        return context


class TopicList(TopicSidebarMixin, ListView):
    context_object_name = 'topics'

    def get_queryset(self):
        return Topic.objects.filter(user=self.request.user)


class TopicDetail(TopicSidebarMixin, DetailView):
    context_object_name = 'current_topic'
    slug_field = 'slug'

    def get_object(self):
        return get_object_or_404(Topic, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(TopicDetail, self).get_context_data(**kwargs)
        topic = get_object_or_404(Topic, slug=self.kwargs['slug'])
        context['topic_quotes'] = Quote.objects.filter(topics=topic)
        return context


class TopicCreate(TopicSidebarMixin, CreateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy('topic_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TopicCreate, self).form_valid(form)


class TopicUpdate(TopicSidebarMixin, UpdateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy('topic_list')

    def get_object(self):
        return get_object_or_404(Topic, user=self.request.user, slug=self.kwargs['slug'])


class TopicDelete(TopicSidebarMixin, DeleteView):
    success_url = reverse_lazy('topic_list')

    def get_object(self):
        return get_object_or_404(Topic, user=self.request.user, slug=self.kwargs['slug'])
