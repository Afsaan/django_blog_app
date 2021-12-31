from django.contrib import admin
from django.urls import path, include
from .views import register, student_create

urlpatterns = [
    path('', register, name='user-register'),
    path('student/', student_create, name='student-register'),



]