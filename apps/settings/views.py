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


def contacts(request):
    setting = Setting.objects.latest('id')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'],form.cleaned_data['content'],'akimjanovalinurr@gmail.com', ['uwu1343@gmail.com'],fail_silently=True)
            if mail:
                messages.success(request,'Письмо отправлено!')
                return redirect('contacts')
            else:
                messages.error(request,'Ошибка отправки')
        else:
            messages.error(request,'Ошибка')
    else:
        form = ContactForm()
    context = {
        'setting' : setting,
        'form' : form
        }
    return render(request, 'courses/contact.html', context)

def job(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
    }
    return render(request,'courses/job-details.html',context)