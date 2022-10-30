from django.urls import path
from .views import index,contact,job,index_dark

urlpatterns = [
    path('', index, name = "index"),
    path('', index_dark, name = "index_dark"),
    path('contacts/', contact, name = "contact"),
    path('job/',job,name="jobs")
]