from uuid import uuid4
import os
from django.shortcuts import render
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from config.settings import MEDIA_ROOT
from django.contrib.auth import authenticate, login, logout
# Create your views here.
class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html")

    def post(self, request):
        # TODO 회원가입
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        User.objects.create(email=email,
                            nickname=nickname,
                            username=username,
                            password=make_password(password),
                            profile_image="default_profile.png")

        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        # TODO 로그인
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        # user = User.objects.filter(email=email).first()
        user = authenticate(email=email, password=password)

        if user is None:
             return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))

        else:
            login(request, user)
            return Response(status=200)


class LogOut(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, "user/login.html")


class UploadProfile(APIView):
    def post(self, request):

        # 일단 파일 불러와
        file = request.FILES['file']
        email = request.data.get('email')

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        profile_image = uuid_name

        user = User.objects.filter(email=email).first()

        user.profile_image = profile_image
        user.save()

        return Response(status=200)
