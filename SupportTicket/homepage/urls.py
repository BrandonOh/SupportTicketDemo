from django.urls import path
from django.contrib.auth import views as auth_views
from .views import loginUser
from . import views

urlpatterns = [
    path('homepage', views.index, name='index'),
    path('', loginUser, name = 'loginUser'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
]