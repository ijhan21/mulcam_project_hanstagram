from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
# Create your views here.
# def index(request):
#     return render(request,'content/main.html')
# def profile(request):
#     return render(request,'content/profile.html')
class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()
        context = dict(feed_list=feed_list)
        return render(request, 'content/main.html', context=context)

class Profile(APIView):
    def get(self, request):
        return render(request, 'content/profile.html')