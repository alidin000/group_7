from django.contrib import admin
from django.urls import path

from .views import AdminPageView, admin_page_view, edit_user_profile, list_students, temp_view, main_page, temp_cookies, register, login_view, logout_view, user_profile

urlpatterns = [
    path('', temp_view, name="temp_form"),
    path('main_page/', main_page, name="main_page"),
    path('temp_cookies/', temp_cookies, name="cookie"),

    # authenticate

    path ('register/', register, name='register'),
    path ('login/', login_view, name='login'),
    path ('logout/', logout_view, name='logout'),

    #  admin page
    path('admin_page/', AdminPageView.as_view(), name='admin_page'),
    path('admin_page_func/', admin_page_view, name='admin_page_func'),


    # students

    path('list/', list_students, name='list'),

    # user_profile view
    path('profile/', user_profile, name='profile'),
    path('profile/edit', edit_user_profile, name='edit_profile'),

]