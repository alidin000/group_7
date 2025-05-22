from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField()

# ORM 

# create table user (
#   name varchar(25)
# );