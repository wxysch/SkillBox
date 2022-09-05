from django.shortcuts import render, redirect
from .models import Course, Teachers
from apps.settings.models import Setting


def course_detail(request, id):
    course = Course.objects.get(id = id)
    setting= Setting.objects.latest('id')
    context={
        'course': course,
        'setting': setting, 
    }
    return render(request, 'courses/course-detail.html', context)
