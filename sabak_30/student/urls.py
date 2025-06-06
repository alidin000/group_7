from django.urls import path
from .views import main_page, student_page, student_by_id

urlpatterns = [
    path('', main_page),
    path('students/', student_page),
    path('student/<str:name>', student_by_id),
]
