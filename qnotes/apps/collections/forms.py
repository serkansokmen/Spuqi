from django import forms
from .models import Collection
from apps.accounts.forms import MemberMultipleChoices
from apps.sources.forms import SourceMultipleChoices


class CollectionForm(forms.ModelForm):
    sources = SourceMultipleChoices()
    members = MemberMultipleChoices()

    class Meta:
        model = Collection
        exclude = ('user',)
