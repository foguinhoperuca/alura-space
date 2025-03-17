from django.urls import path
from custom_users.views import login, register


urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register')
]
