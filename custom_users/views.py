from typing import Dict

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from custom_users.forms import LoginForms, RegisterForms


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
                msg = f'User was authenticated'
                print(msg)
                messages.success(request, msg)
                return redirect('index')
            else:
                msg = f"Can't authenticate the folling user: {form['username'].value()}"
                print(msg)
                messages.error(request, msg)
                return redirect('login')

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

            if User.objects.filter(username=form['username'].value()).exists():
                return redirect('register')

            # print(form['username'].value())
            # print(form['email'].value())
            # print(form['password'].value())
            # print(form['confirm_password'].value())
            user = User.objects.create_user(username=form['username'].value(), email=form['email'].value(), password=form['password'].value())
            user.save()

            return redirect('login')

    return render(request, 'custom_users/register.html', context)
