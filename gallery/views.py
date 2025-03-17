from django.shortcuts import render
from django.http import HttpResponse

from gallery.models import Photograph


def index(request):
    data = {
        1: {
            "name": "Carina's nebulosa",
            "legend": "webtelescope.org / NASA / James Webb"
        },
        2: {
            "name": "Galaxy NGC 1079",
            "legend": "nasa.org / NASA / Hubble"
        }
    }

    data_models = Photograph.objects.all()

    # return render(request, 'gallery/index.html', {"cards": data})
    return render(request, 'gallery/index.html', {"cards": data_models})


def image(request):
    return render(request, 'gallery/image.html')


def search(request):
    # FIXME order by date instead name and filter by published
    photos = Photograph.objects.order_by("name")

    if "search" in request.GET:
        name_to_search = request.GET['search']
        if name_to_search:
            photos = photos.filter(name__icontains=name_to_search)

    return render(request, 'gallery/search.html', {"cards": photos})
