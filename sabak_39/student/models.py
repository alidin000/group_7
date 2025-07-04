from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField(max_length=90)

    def __str__(self):
        return f"{self.name}: {self.email}"
    

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=26, blank=True, null=True)

    tuulgan_kun = models.DateField(blank=True, null=True)

