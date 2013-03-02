from django import forms
from .models import Source
from apps.authors.forms import AuthorChoices
from django_select2.fields import AutoModelSelect2Field


class SourceChoices(AutoModelSelect2Field):
    queryset = Source.objects
    search_fields = ['title__icontains', ]


class SourceForm(forms.ModelForm):

    authors = AuthorChoices()

    class Meta:
        model = Source
        exclude = ('user',)
