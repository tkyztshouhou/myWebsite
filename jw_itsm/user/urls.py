from django.urls import path
from user import views

urlpatterns = [
    path('',views.login),
    path('login/', views.login),
    path('index/', views.index),
    path('process/', views.process),
]