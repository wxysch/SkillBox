from django.urls import path
from .views import Course,course_search,course_detail,course_grid,all_teachers,teacher_detail,course_search,buy_course

urlpatterns = [
    path('', Course, name='courses'),
    path('course/<int:id>/',course_detail ,name="course_detail" ),
    path('search/', course_search, name="search"),
    path('course-grid/', course_grid, name = "grid"),
    path('teachers/', all_teachers, name="teachers-all"),
    path('teachers-detail/<int:id>', teacher_detail, name="teachers-detail"),
    path('buy_course/', buy_course,name="bank")
] 