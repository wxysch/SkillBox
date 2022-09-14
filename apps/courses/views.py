from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from .models import Course, Teachers,Comment
from apps.settings.models import Setting
from django.http import HttpResponse
from django.db.models import Q

def course_detail(request, id):
    course = Course.objects.get(id = id)
    setting= Setting.objects.latest('id')
    comments = Comment.objects.all()
    if request.method == "POST":
        text = request.POST.get('text')
        Comment.objects.create(user = request.user, comment_user = course, text = text)
        return redirect('course_detail', course.id)
    context={
        'course': course,
        'setting': setting, 
        'comments' : comments,
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


def course_grid(request):
    setting = Setting.objects.latest('id')
    courses = Course.objects.all()
    context = {
        'setting' : setting,
        'courses': courses
    }
    return render(request,'courses/course-grid.html', context)

def teacher_detail(request, id):
    setting = Setting.objects.latest('id')
    teacher = Teachers.objects.get(id = id)
    context = {
        'setting' : setting,
        'teacher' : teacher,
    }
    return render(request,'courses/teachers-detail.html', context)

def all_teachers(request):
    setting = Setting.objects.latest('id')
    teachers = Teachers.objects.all()
    context = {
        'setting' : setting,
        'teachers' : teachers,
    }
    return render(request,'courses/all-teachers.html', context)

def course_search(request):
    setting = Setting.objects.latest('id')
    courses = Course.objects.all()
    comments = Comment.objects.all()
    qury_object = request.GET.get('key')
    if qury_object:
        courses = Course.objects.filter(Q(name__icontains = qury_object))
    context = {
        'setting' : setting,
        'courses' : courses,
        'comments' : comments,
    }
    return render(request,"courses/search.html", context)

def buy_course(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
    }
    return render(request, 'courses/bank.html',context)