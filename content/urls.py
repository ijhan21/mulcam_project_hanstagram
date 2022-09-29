from django.urls import path
from . import views
app_name = 'content'
urlpatterns = [
    path('', views.Main.as_view(), name='index'),
    path('content/profile', views.Profile.as_view(), name='profile'),
]
