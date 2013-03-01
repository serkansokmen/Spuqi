from django import forms
from .models import Source
from apps.authors.models import Author
from django_select2.fields import AutoModelSelect2MultipleField


class AuthorChoices(AutoModelSelect2MultipleField):
    queryset = Author.objects
    search_fields = ['name__icontains', ]


class SourceForm(forms.ModelForm):

    authors = AuthorChoices()

    class Meta:
        model = Source
        exclude = ('user',)
