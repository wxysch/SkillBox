from django.urls import path
from .views import index,contact,job

urlpatterns = [
    path('', index, name = "index"),
    path('contacts/', contact, name = "contact"),
    path('job/',job,name="jobs")
]