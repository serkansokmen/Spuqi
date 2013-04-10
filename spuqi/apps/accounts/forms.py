from django import forms
from django.utils.translation import ugettext as _


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label=_('First Name'))
    last_name = forms.CharField(max_length=30, label=_('Last Name'))

    def __init__(self, *args, **kwargs):
        """
        A bit of hackery to get the first name and last name at the top of the
        form instead at the end.
        """
        super(SignupForm, self).__init__(*args, **kwargs)

        # Put the first and last name at the top
        order = self.fields.keyOrder[:-7]
        order.insert(0, 'username')
        order.insert(0, 'first_name')
        order.insert(1, 'last_name')
        order.insert(3, 'email')
        order.insert(4, 'password1')
        order.insert(5, 'password2')
        self.fields.keyOrder = order

    def save(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
