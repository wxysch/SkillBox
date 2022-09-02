from django.urls import path
from .views import Course,course_detail

urlpatterns = [
    path('', Course, name='courses'),
    path('course/<int:id>/',course_detail ,name="course_detail" ),
]