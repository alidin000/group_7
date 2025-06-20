from django.urls import path

from .views import course, student
urlpatterns = [
    path('', student, name="student"),
    path('courses/', course, name="course"),
]
