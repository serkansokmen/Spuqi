from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import Collection
from apps.accounts.forms import MemberChoices
from apps.sources.forms import SourceChoices


class CollectionForm(forms.ModelForm):
    sources = SourceChoices()
    members = MemberChoices()

    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Collection
        exclude = ('user',)
        widgets = {
            'sources': CheckboxSelectMultiple(),
            'members': CheckboxSelectMultiple(),
        }
