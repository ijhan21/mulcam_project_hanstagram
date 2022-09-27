from django.urls import path
from . import views
app_name = 'content'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
]
