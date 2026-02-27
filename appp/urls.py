from django.contrib import admin

from django.urls import path,include
from . import views

urlpatterns = [
  
    path('home/', views.home, name='home'),
    path('colleges/', views.colleges, name='colleges'),
    path('students/', views.students, name='students'),
    path('address/', views.address, name='address'),
    path('send_email/',views.send_email,name='send_email')
]
