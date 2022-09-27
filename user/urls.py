from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'
urlpatterns = [
    path('join', views.Join.as_view(), name='join'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.LogOut.as_view(), name='logout'),
]
