from django.urls import path
from .views import Course,course_search,course_detail,course_grid,all_teachers

urlpatterns = [
    path('', Course, name='courses'),
    path('course/<int:id>/',course_detail ,name="course_detail" ),
    path('', course_search, name="search"),
    path('course-grid/', course_grid, name = "grid"),
    path('teachers/', all_teachers, name="teachers-all")
] 