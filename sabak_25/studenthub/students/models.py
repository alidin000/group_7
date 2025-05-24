from django.db import models

# Create your models here.

class Students(models.Model):
    # django ozu id attribute koshup koiot => id = models.AutoField(primary_key=True, **options)
    # jana oshol primary key  bolot 

    # primary key = unique = ozgoho 

    first_name = models.CharField(max_length=30, primary_key=True, db_column="Name")
    last_name = models.CharField(max_length=30)

    age = models.IntegerField()

    tuulgan_kun = models.DateField()


# insert into students (id,name, last_name, age, tuulgan kun)
# values (0, "tekebai", "omurbek", 44, 2000.01.01)

# insert into students (id,name, last_name, age, tuulgan kun)
# values (0, "tekebai", "omurbek", 44, 2000.01.01)

# table already contains row with primary key 0