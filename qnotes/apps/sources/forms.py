from django import forms
from .models import Source


class SourceForm(forms.ModelForm):

    class Meta:
        model = Source
        exclude = ('user', 'slug', )
