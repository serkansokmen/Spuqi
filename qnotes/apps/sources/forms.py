from django import forms
from qnotes.apps.sources.models import Source


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        exclude = ('user',)
