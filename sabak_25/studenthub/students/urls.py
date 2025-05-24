from django.urls import path

# from studenthub.students.views import hello_student
from .views import hello_student, list_students

urlpatterns = [
    path('hello/', hello_student),
    path('list_students', list_students)
]