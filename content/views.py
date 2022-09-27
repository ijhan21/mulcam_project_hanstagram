from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'content/main.html')
def profile(request):
    return render(request,'content/profile.html')
