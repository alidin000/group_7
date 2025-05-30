from django.urls import path
from .views import simple_html, main_page, TempView, json, temp, get_id, get_name,get_student

urlpatterns = [
    path('html/', simple_html),
    path("", main_page),
    path('classbased/', TempView.as_view()),
    path('json/', json),
    path('name/', temp),
    path('temp/<int:id>/', get_id),
    path('temp/<str:name>/', get_name),
    path('list/',get_student)
]
