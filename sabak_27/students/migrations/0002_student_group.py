# Generated by Django 5.2.1 on 2025-05-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.CharField(default='7'),
        ),
    ]
