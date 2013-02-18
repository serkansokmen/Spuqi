from django import forms
from qnotes.apps.topics.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        exclude = ('user',)
