from django.contrib import admin
from django.urls import path

from .views import temp_view

urlpatterns = [
    path('', temp_view, name="temp_form"),
]