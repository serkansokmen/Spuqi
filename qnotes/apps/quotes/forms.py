from django import forms
from django.forms import Textarea
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from qnotes.apps.quotes.models import Quote


class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        exclude = ('user',)
        widgets = {
            'quote': Textarea(attrs={'rows': 6, 'class': 'input-xxlarge'}),
            'note': Textarea(attrs={'rows': 4, 'class': 'input-xlarge'}),
            'source': RadioSelect(),
            'topics': CheckboxSelectMultiple(),
        }
