from django.db import models
from django.db.models import Model
# Create your models here.

class Student(Model):
    name = models.CharField()

    group = models.CharField(default="7")
    def __str__(self):
        return self.name
