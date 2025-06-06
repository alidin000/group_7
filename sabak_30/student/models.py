from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f" {self.code} - {self.name}"

class Student(models.Model):
    name  = models.CharField(max_length=50)
    email  = models.EmailField(unique=True)
    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='student_photos/'
    )
    courses = models.ManyToManyField(Course, blank=True, related_name='student')
    def __str__(self):
        return self.name
    

