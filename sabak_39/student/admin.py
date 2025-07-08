from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Student, CustomUser, UserProfile

admin.site.register(Student)
admin.site.register(UserProfile)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'tuulgan_kun', 'profile_picture')}),
    )