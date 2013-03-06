from django import forms
from django.contrib.auth.models import User
from .models import Collection


class CollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        exclude = ('user', 'slug', )

    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        self.fields['members'].queryset = User.objects.filter(id__gt=-1)
