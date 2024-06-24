from django.urls import path
from . import views

urlpatterns = [
    path('', views.joke_home, name='joke_home'),
    path('register/', views.register, name='register'),

]
