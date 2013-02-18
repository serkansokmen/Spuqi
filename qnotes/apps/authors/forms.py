from django import forms
from qnotes.apps.authors.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ('user',)
