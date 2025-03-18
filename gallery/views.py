from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from gallery.models import Photograph


def index(request):
    data_models = Photograph.objects.filter(published=True).order_by('-photo_date')

    return render(request, 'gallery/index.html', {"cards": data_models})


def image(request, photo_id: int):
    print(f'got {photo_id=}')
    photo = get_object_or_404(Photograph, pk=photo_id)

    print(f'{photo=}')
    return render(request, 'gallery/image.html', {"photo": photo})


def search(request):
    photos = Photograph.objects.order_by("photo_date").filter(published=True)

    if "search" in request.GET:
        name_to_search = request.GET['search']
        if name_to_search:
            photos = photos.filter(name__icontains=name_to_search)

    return render(request, 'gallery/search.html', {"cards": photos})
