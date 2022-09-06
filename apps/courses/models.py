from tkinter import CASCADE
from django.db import models

# Create your models here.
class Language(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки" 

class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    course_image = models.ImageField(upload_to = "course_image")
    price = models.IntegerField()
    languages = models.ForeignKey(Language,max_length=255,on_delete=models.CASCADE)
     
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы" 

class Teachers(models.Model):
    name = models.CharField(max_length=155)
    job_title = models.CharField(max_length=150) 
    bio = models.TextField()
    age = models.SmallIntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to = 'teachers')
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"