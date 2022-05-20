from django import views
from django.urls import path, include
from clientprofile import views

app_name = 'clientprofile'

urlpatterns = [
    path('clients/', views.ClientList_view.as_view()),
    path('clients/<int:pk>/', views.ClientDetail_view.as_view()),
]