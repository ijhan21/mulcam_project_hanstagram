from django.urls import path
from . import views
app_name = 'content'
urlpatterns = [
    path('', views.index, name='index'),
    path('content/profile', views.profile, name='profile'),
]
