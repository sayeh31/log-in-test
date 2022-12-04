from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.view_login_page),
    path('form/', views.form),]
 