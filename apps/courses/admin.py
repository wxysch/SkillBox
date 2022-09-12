from django.contrib import admin
from .models import Course,Language,Teachers,Comment
# Register your models here.
admin.site.register(Course)
admin.site.register(Language)
admin.site.register(Teachers)
admin.site.register(Comment)