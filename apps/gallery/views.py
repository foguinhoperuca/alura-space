from typing import Dict

from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from apps.gallery.models import Photograph
from apps.gallery.forms import PhotographForms


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User is not logged!!')
        return redirect('login')

    data_models = Photograph.objects.filter(published=True).order_by('-photo_date')

    return render(request, 'gallery/index.html', {"cards": data_models})


def image(request, photo_id: int):
    print(f'got {photo_id=}')
    photo = get_object_or_404(Photograph, pk=photo_id)

    print(f'{photo=}')
    return render(request, 'gallery/image.html', {"photo": photo})


def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User is not logged!!')
        return redirect('login')

    photos = Photograph.objects.order_by("photo_date").filter(published=True)

    if "search" in request.GET:
        name_to_search = request.GET['search']
        if name_to_search:
            photos = photos.filter(name__icontains=name_to_search)

    return render(request, 'gallery/search.html', {"cards": photos})


def new(request):
    context: Dict[str, str] = {}
    form: PhotographForms = PhotographForms()
    context['form'] = form

    if not request.user.is_authenticated:
        messages.error(request, 'User is not logged!!')
        return redirect('login')

    if request.method == 'POST':
        form = PhotographForms(request.POST, request.FILES)
        context['form'] = form

        if form.is_valid():
            form.save()
            messages.success(request, 'New photo was added!!')

            return redirect('index')
        else:
            messages.error(request, 'The form has some errors. Please, fix it!!')

    return render(request, 'gallery/new.html', context)


def edit(request, photo_id: int):
    context: Dict[str, str] = {}
    photo: Photograph = Photograph.objects.get(id=photo_id)
    form: PhotographForms = PhotographForms(instance=photo)
    context['form'] = form
    context['photo_id'] = photo_id

    if request.method == 'POST':
        form = PhotographForms(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo was edited with success!!')

            return redirect('index')
        else:
            messages.error(request, "The editions has some error. Please, fix it!")

    return render(request, 'gallery/edit.html', context)


def delete(request):
    context: Dict[str, str] = {}

    return render(request, 'gallery/delete.html', context)
