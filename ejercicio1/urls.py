from django.urls import path

from .import views

urlpatterns = [
    path('ejercicio1/', views.holamundo, name='holamundo'),
]