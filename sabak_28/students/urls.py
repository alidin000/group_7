from django.urls import path
from .views import base_html, head_html

urlpatterns = [
    path('', base_html),
    path('head/',head_html)
]
