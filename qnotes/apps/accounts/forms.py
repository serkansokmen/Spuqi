from django import forms
from django.utils.translation import ugettext_lazy as _
from userena.forms import SignupForm, AuthenticationForm
from captcha.fields import ReCaptchaField


class SignupFormReCaptcha(SignupForm):
    # first_name = forms.CharField(label=_(u'First name'),
    #                              max_length=30,
    #                              required=True)

    # last_name = forms.CharField(label=_(u'Last name'),
    #                             max_length=30,
    #                             required=True)

    capctha = ReCaptchaField(attrs={'theme': 'white'})
    '''
    def __init__(self, *args, **kwargs):
        super(SignupFormReCaptcha, self).__init__(*args, **kwargs)
        # Put the first and last name at the top
        new_order = self.fields.keyOrder[:-3]
        new_order.insert(0, 'first_name')
        new_order.insert(1, 'last_name')
        new_order.insert(2, 'captcha')
        self.fields.keyOrder = new_order

    def save(self):
        # First save the parent form and get the user.
        new_user = super(SignupFormReCaptcha, self).save()

        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.save()

        # Userena expects to get the new user from this form, so return the new
        # user.
        return new_user
    '''


class SigninFormReCaptcha(AuthenticationForm):

    # capctha = ReCaptchaField(attrs={'theme': 'white'})

    def __init__(self, *args, **kwargs):
        super(SigninFormReCaptcha, self).__init__(*args, **kwargs)
