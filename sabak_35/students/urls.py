from django.urls import path

from .views import students_list, student_add, student_update, student_delete, student_put

urlpatterns = [
    path('', students_list, name="students_list"),
    path('add/', student_add, name="student_add"),
    path('update/<int:id>', student_update, name="student_update"),
    path('delete/<str:name>', student_delete, name="student_delete"),
    path('put/<str:name>', student_put, name="student_put"),
]