from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('login', loginUser, name = 'loginUser'),
    path('homepage', index, name='index'),
    path('logout',logoutUser, name='logoutUser'),
]