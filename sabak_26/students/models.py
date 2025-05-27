from django.db import models

# Create your models here.
class Student(models.Model):
    aty = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    tuulgan_kunu = models.DateField()

    def __str__(self):
        return f"{self.aty}"
    
    