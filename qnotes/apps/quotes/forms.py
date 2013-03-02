from django import forms
from django.forms import Textarea
from .models import Quote
from apps.sources.forms import SourceChoices
from apps.topics.forms import TopicMultipleChoices


class QuoteForm(forms.ModelForm):
    source = SourceChoices()
    topics = TopicMultipleChoices(required=False)
    tags = forms.TextInput()

    class Meta:
        model = Quote
        exclude = ('user', 'note_type', 'tags',)
        widgets = {
            'quote': Textarea(attrs={'rows': 6, 'class': 'input-xxlarge'}),
            'note': Textarea(attrs={'rows': 4, 'class': 'input-xlarge'}),
            # 'tags': Select2MultipleWidget()
        }
