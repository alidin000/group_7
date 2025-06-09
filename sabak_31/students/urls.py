from django.urls import path
from .views import get_students, temp_func, first_form

urlpatterns = [
    path('', temp_func),
    path('first_form/', first_form, name="first_form"),
    path('get_students/', get_students, name="get_students"),
]