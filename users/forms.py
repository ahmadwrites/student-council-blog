from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Password


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:  # Model to interact with
        model = User  # Going to save to this User model
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']


class PasswordForm(forms.ModelForm):
    password = forms.CharField(label='Password (confirmation)', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'type': 'password'}))

    class Meta:
        model = Password
        fields = ['password']
