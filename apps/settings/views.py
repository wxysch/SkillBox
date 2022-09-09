from re import I
from django.shortcuts import render
from .models import Setting,ItRunLogo
from apps.courses.models import Course,Language,Teachers
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    it_run = ItRunLogo.objects.latest('id')
    courses = Course.objects.all()
    language = Language.objects.all()
    teachers = Teachers.objects.all()
    context = {
        'setting' : setting,
        'it_run' : it_run,
        'courses' : courses,
        'language' : language,
        'teachers' : teachers,
    }
    return render(request, 'courses/index.html', context)


def contacts(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
        }
    return render(request, 'courses/contact.html', context)

def job(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
    }
    return render(request,'courses/job-details.html',context)