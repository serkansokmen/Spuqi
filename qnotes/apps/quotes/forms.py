from django import forms
from django.forms import Textarea
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
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

    def clean(self):
        if Quote.objects.filter(
            quote=self.cleaned_data['quote'],
            source=self.cleaned_data['source']
        ).count() > 0:
            msg = mark_safe(
                '%s' % _('This quotation is already created.')
            )
            raise forms.ValidationError(msg)
        return self.cleaned_data
