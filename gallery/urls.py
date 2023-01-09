from django.urls import path
from gallery.views import index, image

urlpatterns = [
    path('', index),
    path('image', image)
]