from django import forms
from django.forms import Textarea
from qnotes.apps.quotes.models import Quote
from qnotes.apps.sources.models import Source
from qnotes.apps.topics.models import Topic
from django_select2.fields import AutoModelSelect2Field, AutoModelSelect2MultipleField


class SourceChoices(AutoModelSelect2Field):
    queryset = Source.objects
    search_fields = ['title__icontains', ]


class TopicChoices(AutoModelSelect2MultipleField):
    queryset = Topic.objects
    search_fields = ['title__icontains', ]


class QuoteForm(forms.ModelForm):
    source = SourceChoices()
    topics = TopicChoices(required=False)
    tags = forms.TextInput()

    class Meta:
        model = Quote
        exclude = ('user',)
        widgets = {
            'quote': Textarea(attrs={'rows': 6, 'class': 'input-xxlarge'}),
            'note': Textarea(attrs={'rows': 4, 'class': 'input-xlarge'}),
            # 'tags': Select2MultipleWidget()
        }
