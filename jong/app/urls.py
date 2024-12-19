from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # หน้าแรก
    path('register/', views.register, name='register'),  # หน้าลงทะเบียน
]
