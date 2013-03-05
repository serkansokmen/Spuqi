from django import forms
from django.utils.translation import ugettext as _
from .models import Source
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Layout, Fieldset, HTML
from crispy_forms.bootstrap import FormActions


class SourceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.layout = Layout(
            Fieldset(
                _('Add new source'),
                'title',
                'authors',
                Button('new-author', "<p>We use notes to get better, <strong>please help us {{ username }}</strong></p>", css_class='btn-success btn-new-author'),
                'url',
                'isbn',
            ),
            FormActions(
                Submit('submit', _('Submit'), css_class='btn-primary'),
                Button('cancel', _('Cancel'))
            )
        )
        super(SourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Source
        exclude = ('user', 'slug', )
