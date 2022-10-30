from django.contrib import messages
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import Setting,ItRunLogo
from apps.courses.models import Course,Language,Teachers
from .forms import ContactForm

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

def index_dark(request):
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
    return render(request, 'courses/index-dark.html', context)

def contact(request):
    form = ContactForm()

    return render(request, 'courses/job-details.html')



def job(request):
    if request.method == 'POST':
        
        form = ContactForm()
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            print('отправлено')
            send_mail('the contact form subject', 'this is the message', 'uwu1343@gmail.com', ['akimjanovalinurr@gmail.com'])
            return redirect('job')
    else:
        form = ContactForm()
    context = {
        'form' : form,
        
    }
    return render(request,'courses/job-details.html',context)