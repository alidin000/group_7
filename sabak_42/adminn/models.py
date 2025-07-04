from django.db import models
from django.contrib.auth.models import AbstractUser
\
# Create your models here.

class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=26, blank=True, null=True)

    tuulgan_kun = models.DateField(blank=True, null=True)
