from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField(max_length=20)