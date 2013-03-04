from django import forms
from .models import Collection


class CollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        exclude = ('user', 'slug', )
