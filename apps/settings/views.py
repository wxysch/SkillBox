from re import I
from django.shortcuts import render
from .models import Setting,ItRunLogo
from apps.courses.models import Course,Language
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    it_run = ItRunLogo.objects.latest('id')
    courses = Course.objects.all()
    language = Language.objects.all()
    context = {
        'setting' : setting,
        'it_run' : it_run,
        'courses' : courses,
        'language' : language
    }
    return render(request, 'courses/index.html', context)
