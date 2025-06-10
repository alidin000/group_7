from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40, unique=True)
    age = models.IntegerField()
    email = models.EmailField()
    attendance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}: {self.email}"