from django.contrib import admin
from .models import Student, Course

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'photo')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)