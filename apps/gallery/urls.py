from django.urls import path
from apps.gallery.views import index, image, search, new, edit, delete

urlpatterns = [
    path('', index, name='index'),
    path('search', search, name='search'),
    path('image/<int:photo_id>', image, name='image'),
    path('image_edit/<int:photo_id>', edit, name='image_edit'),
    path('new', new, name='image_new'),
    path('delete', delete, name='image_delete'),
]
