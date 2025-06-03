from django.urls import path
from .views import main, base, child_base

urlpatterns = [
    path('', main),
    path('base/', base),
    path('child_base/', child_base),
]
