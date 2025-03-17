from typing import Dict

from django.shortcuts import render


def login(request):
    context: Dict = {}

    return render(request, 'custom_users/login.html', context)


def register(request):
    context: Dict = {}

    return render(request, 'custom_users/register.html', context)
