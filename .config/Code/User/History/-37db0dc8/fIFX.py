from django import views
from django.urls import path, include
from clientprofile import views

app_name = 'clientprofile'

urlpatterns = [
    path('client/', views.client_view.as_view()),
]