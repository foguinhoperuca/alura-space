from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'gallery/index.html')


def image(request):
    return render(request, 'gallery/image.html')
