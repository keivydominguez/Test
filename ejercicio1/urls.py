from django.urls import path

from .import views

urlpatterns = [
    path('ejercicio1/', views.holamundo, name='holamundo'),
    path('ejercicio1/numeromedio/', views.numero_medio, name='numeromedio'),

]