from typing import Dict

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from apps.custom_users.forms import LoginForms, RegisterForms


def login(request):
    context: Dict = {}
    form: LoginForms = LoginForms()
    context['form'] = form

    if request.method == 'POST':
        form = LoginForms(request.POST)
        username: str = form['username'].value()
        password: str = form['password'].value()
        print(f'{username=}')
        print(f'{password=}')

        msg: str = ''
        if form.is_valid():
            user = auth.authenticate(request, username=username, password=password)
            print(f'{user=}')
            if user is not None:
                auth.login(request, user)
                msg = f'User was authenticated {form["username"].value()}'
                print(msg)
                messages.success(request, msg)
                return redirect('index')
            else:
                msg = f"Can't authenticate the following user: {form['username'].value()}"
                print(msg)
                messages.error(request, msg)
                return redirect('login')

    return render(request, 'custom_users/login.html', context)


def logout(request):
    auth.logout(request)
    msg: str = 'Logout was successfully!!'
    print(msg)
    messages.success(request, msg)

    return redirect('login')


def register(request):
    context: Dict = {}
    form: RegisterForms = RegisterForms()
    context['form'] = form

    if request.method == 'POST':
        form = RegisterForms(request.POST)
        context['form'] = form

        msg: str = ''
        if form.is_valid():
            # TODO move it to run validations in forms
            if form['password'].value() != form['confirm_password'].value():
                msg = 'Invalid password: confirmation do not match!!'
                print(msg)
                messages.error(request, msg)

                return redirect('register')

            if User.objects.filter(username=form['username'].value()).exists():
                msg = f'User {form["username"].value()} already exists!!'
                print(msg)
                messages.error(request, msg)

                return redirect('register')

            user = User.objects.create_user(username=form['username'].value(), email=form['email'].value(), password=form['password'].value())
            user.save()
            msg = f'User {form["username"].value()} was successfully created!!'
            print(msg)
            messages.success(request, msg)

            return redirect('login')
        else:
            msg = 'Invalid data! Please fix it!!'
            print(msg)
            messages.error(request, msg)

    return render(request, 'custom_users/register.html', context)
