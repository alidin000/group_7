from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    group = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.name}: {self.email}"
    

