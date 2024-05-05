from allauth.account.forms import SignupForm
from django import forms


class CustomSignUpForm(SignupForm):
    phone_number = forms.IntegerField(label='Телефон')

    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user
