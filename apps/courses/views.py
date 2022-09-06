from django.shortcuts import render, redirect
from .models import Course, Teachers
from apps.settings.models import Setting
from django.http import HttpResponse

def course_detail(request, id):
    course = Course.objects.get(id = id)
    setting= Setting.objects.latest('id')
    context={
        'course': course,
        'setting': setting, 
    }
    return render(request, 'courses/course-detail.html', context)

def update(request, id):
    setting = Setting.objects.latest('id')
    course = Course.objects.get(id=id)
    if request.method == "POST":
        try:
            name = request.FILES.get('name')
            description = request.POST.get('description')
            course_image = request.POST.get('course_image')
            price = request.POST.get('price')
            languages = request.POST.get('currency')
            course = Course.objects.get(id=id)
            course.name = name
            course.description = description
            course.price = price 
            course.course_image = course_image
            course.languages = languages 
            course.save()
            return redirect('post_detail', course.id)
        except:
            return HttpResponse("Error")
    context = {
        'setting' : setting,
        'course' : course,
    }
    return render(request, 'courses/update.html', context)