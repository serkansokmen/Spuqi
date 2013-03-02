from django import forms
from .models import Author
from django_select2.fields import AutoModelSelect2Field, AutoModelSelect2MultipleField


class AuthorChoices(AutoModelSelect2Field):
    queryset = Author.objects
    search_fields = ['name__icontains', ]


class AuthorMultipleChoices(AutoModelSelect2MultipleField):
    queryset = Author.objects
    search_fields = ['name__icontains', ]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ('user',)
