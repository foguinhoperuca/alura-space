from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse('<h1>Alura Space</h1><p>Welcome to Space!!</p>')
    return render(request, 'index.html')


def image(request):
    return render(request, 'image.html')
