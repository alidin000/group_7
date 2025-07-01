from django.contrib import admin
from django.urls import path

from .views import temp_view, main_page, temp_cookies

urlpatterns = [
    path('', temp_view, name="temp_form"),
    path('main_page', main_page, name="main_page"),
    path('temp_cookies', temp_cookies, name="cookie"),
]