from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    tags = forms.TextInput()

    class Meta:
        model = Quote
        exclude = ('user', 'slug',)
        widgets = {
            'quote': forms.Textarea(attrs={'rows': 6}),
            # 'tags': Select2MultipleWidget()
            # 'privacy_state': forms.RadioSelect()
        }
