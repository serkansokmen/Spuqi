from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from qnotes.apps.collections.models import Collection
from libs.utils import remove_holddown


class CollectionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        remove_holddown(self, self.fields)

    class Meta:
        model = Collection
        exclude = ('user',)
        widgets = {
            'sources': CheckboxSelectMultiple(),
            'members': CheckboxSelectMultiple(),
        }
