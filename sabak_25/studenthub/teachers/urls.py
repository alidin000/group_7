from django.urls import path
from .views import homeworks


urlpatterns = [
    path('homeworks/', homeworks)
]
