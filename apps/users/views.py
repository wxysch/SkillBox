from django.shortcuts import render, redirect
from apps.settings.models import Setting
from .models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        profile_image = request.FILES.get('profile_image')
        if password1 == password2:
            user = User.objects.create(username = username, profile_image = profile_image, email = email)
            user.set_password(password1)
            user.save()
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password1)
            login(request, user)
            return redirect('index')
           
        else:
            return HttpResponse("Пароли не совпадают")

    context = {
        'setting' : setting,
    }
    return render(request, 'users/register.html', context)

def user_login(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        except:
            return HttpResponse("Неправильные данные")
    
    context = {
        'setting' : setting,
    }
    return render(request, 'users/login.html', context)

def profile(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
    }
    return render(request,'courses/profile.html', context)