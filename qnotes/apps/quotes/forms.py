from django import forms
from django.forms import Textarea
from .models import Quote


class QuoteForm(forms.ModelForm):
    tags = forms.TextInput()

    class Meta:
        model = Quote
        exclude = ('user', 'slug', 'tags',)
        widgets = {
            'quote': Textarea(attrs={'rows': 6}),
            # 'tags': Select2MultipleWidget()
        }
