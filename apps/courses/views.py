from django.shortcuts import render, redirect
from apps.settings.models import Setting
from .models import Course
# Create your views here.
def courses(request):
    setting = Setting.objects.latest('id')
    courses = Course.objects.all()
    context = {
        'setting' : setting,
        'course' : courses,
    }
    return render(request,'courses/index.html', context)