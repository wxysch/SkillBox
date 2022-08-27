from django.shortcuts import render
from .models import Setting,ItRunLogo
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    it_run_logo = ItRunLogo.objects.get()
    context = {
        'setting' : setting,
        'it_run_logo' : it_run_logo
    }
    return render(request, 'courses/index.html', context)
