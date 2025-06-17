from django.urls import path

from .views import get_student, get_students

urlpatterns = [
    path('api/students', get_students, name="get_students"),
    path('api/student', get_student, name="get_student"),
]
