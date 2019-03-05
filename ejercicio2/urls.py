from django.urls import path
from . import views

urlpatterns = [
    path('ejercicio2/', views.fecha, name='fecha'),
]
