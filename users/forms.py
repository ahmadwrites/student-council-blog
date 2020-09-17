from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Password


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:  # Model to interact with
        model = User  # Going to save to this User model
        fields = ['username', 'email', 'password1', 'password2']


class PasswordForm(forms.ModelForm):
    password = forms.CharField(required=False, label='',
                               widget=forms.TextInput(attrs={'id': 'confirmation',
                                                                   'type': 'password',
                                                             'style': 'display:none;'}))

    class Meta:
        model = Password
        fields = ['password']
