from django.urls import path
from .views import hello_json
urlpatterns = [
    path('', hello_json, name='hello_json'),
]
