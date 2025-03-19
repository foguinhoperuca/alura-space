from typing import Dict

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from custom_users.forms import LoginForms, RegisterForms


def login(request):
    context: Dict = {}
    form: LoginForms = LoginForms()
    context['form'] = form

    return render(request, 'custom_users/login.html', context)


def register(request):
    context: Dict = {}
    form: RegisterForms = RegisterForms()
    context['form'] = form

    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            if form['password'].value() != form['confirm_password'].value():
                return redirect('register')

            if User.objects.filter(username=form['name_login']).exists():
                return redirect('register')

            user = User.objects.create_user(username=form['name_login'], email=form['email'], password=['password'])
            print(f'{user=}')
            # TODO implement it!
            # user.save()

            return redirect('login')

    return render(request, 'custom_users/register.html', context)
