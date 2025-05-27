from django.urls import path
from .views import list_students

urlpatterns = [
    path('student/', list_students),
]
