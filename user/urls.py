from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    #user/로 들어온 경우
    path('', views.UserView.as_view()),
    path('login/', views.UserAPIView.as_view()),
]
