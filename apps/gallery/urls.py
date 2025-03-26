from django.urls import path
from apps.gallery.views import index, image, search, new, edit, delete, image_filter

urlpatterns = [
    path('', index, name='index'),
    path('search', search, name='search'),
    path('filter/<str:category>', image_filter, name='image_filter'),
    path('image_new', new, name='image_new'),
    path('image/<int:photo_id>', image, name='image'),
    path('image/<int:photo_id>/edit', edit, name='image_edit'),
    path('image/<int:photo_id>/delete', delete, name='image_delete'),
]
