from django import forms
from .models import Email


class EmailForm(forms.ModelForm):
    email = forms.EmailField(label='',
                             widget=forms.EmailInput
                             (attrs={'id': 'email-input', 'class': 'form-control',
                                     'placeholder': 'username@email.com', 'type': 'email'}))

    class Meta:
        model = Email
        fields = ['email']

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        qs = Email.objects.filter(email__iexact=email)

        if qs.exists():
            raise forms.ValidationError('This email already exists.')

        return email
