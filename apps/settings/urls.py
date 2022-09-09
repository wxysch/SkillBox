from django.urls import path
from .views import index,contacts,job

urlpatterns = [
    path('', index, name = "index"),
    path('contacts/', contacts, name = "contacts"),
    path('job/',job,name="jobs")
]