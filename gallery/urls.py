from django.urls import path
from gallery.views import index, image, search

urlpatterns = [
    path('', index, name='index'),
    path('image', image, name='image'),
    path('search', search, name='search')
]
