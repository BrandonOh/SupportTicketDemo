from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('homepage', index, name='index'),
    path('', loginUser, name = 'loginUser'),
    path('logout/',logoutUser, name='logout'),
]