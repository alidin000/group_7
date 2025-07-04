from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'tuulgan_kun')}),
    )