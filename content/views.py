import email
from multiprocessing import context
import profile
from uuid import uuid4
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from config import settings
import os
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
        feed_count = Feed.objects.filter(email=request.user).count()
        context = {'feed_count':feed_count}
        return render(request, 'content/profile.html', context=context)

class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(settings.MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.data.get('content')
        image = uuid_name
        user_id = request.data.get('user_id')
        create_date = timezone.now()
        user = User.objects.get(email='hans')#[0]
        Feed.objects.create(email=user, content=content,image=image, create_date=create_date)
        return Response(status=200)

@login_required(login_url='user:login')    
def like_count(request, id):
    feed = Feed.objects.get(id=id)
    if request.user.username == feed.email.username:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        if feed.likes.filter(email=request.user):
            feed.likes.remove(request.user)
        else:
            feed.likes.add(request.user)
    return redirect('content:index')