from django import forms
from .models import Email, Comment


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


class CommentForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Add your comment here', 'type': 'text'}))

    class Meta:
        model = Comment
        fields = ['text']
