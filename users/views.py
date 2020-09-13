from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, PasswordForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        p_form = PasswordForm(request.POST)
        if form.is_valid():
            form.save()
            passcode = p_form.save(commit=False)
            username = form.cleaned_data.get('username')
            passcode.username = username
            passcode.save()
            messages.success(request, f'{username} has successfully been created.')
            return redirect('login')
    else:
        form = UserRegisterForm()
        p_form = PasswordForm()

    context = {
        'title': 'Register',
        'form': form,
        'p_form': p_form,
    }

    return render(request, 'users/register.html', context)

