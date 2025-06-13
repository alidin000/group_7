from django.urls import path
from .views import create_student, find_student, get_students, hello_json, get_students_post_man
urlpatterns = [
    path('', hello_json, name='hello_json'),
    path('list_students/', get_students, name='list_students'),
    path('list_students_post_man/', get_students_post_man, name='list_students_post_man'),
    path('create_student/', create_student, name='create_student'),
    path('find/', find_student, name="find_student"),
]
