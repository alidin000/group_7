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


from django.conf import settings


class UserProfile (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"Profile : {self.user.username} ({self.user.tuulgan_kun})"