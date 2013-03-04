from django import forms
from django.forms import Textarea
from .models import Quote


class QuoteForm(forms.ModelForm):
    tags = forms.TextInput()

    class Meta:
        model = Quote
        exclude = ('user', 'slug', 'tags',)
        widgets = {
            'quote': Textarea(attrs={'rows': 6, 'class': 'input-xxlarge'}),
            'note': Textarea(attrs={'rows': 4, 'class': 'input-xlarge'}),
            # 'tags': Select2MultipleWidget()
        }
