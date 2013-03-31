import pyisbn
from django import forms
from django.utils.translation import ugettext as _
from .models import Source


class SourceForm(forms.ModelForm):

    class Meta:
        model = Source
        exclude = ('user', 'slug', )

    def clean_isbn(self):
        # validate isbn
        isbn_str = self.cleaned_data['isbn']
        if len(isbn_str) > 0:
            try:
                isbn = pyisbn.Isbn(isbn_str)
            except pyisbn.IsbnError:
                raise forms.ValidationError(
                    _('ISBN number must contain only digit-numbers'))
            else:
                if not isbn.validate():
                    raise forms.ValidationError(
                        _('A valid ISBN number is required'))
                return isbn.isbn
        return isbn_str
