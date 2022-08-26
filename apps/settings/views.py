from django.shortcuts import render
from .models import Setting
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
    }
    return render(request, 'courses/index.html', context)