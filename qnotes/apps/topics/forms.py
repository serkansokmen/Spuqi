from django import forms
from .models import Topic
from django_select2.fields import AutoModelSelect2MultipleField


class TopicChoices(AutoModelSelect2MultipleField):
    queryset = Topic.objects
    search_fields = ['title__icontains', ]


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        exclude = ('user',)
