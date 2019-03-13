from django.urls import path
from . import views

urlpatterns = [
    path('ejercicio2/', views.fecha, name='fecha'),
    path('ejercicio2/abc/', views.abc, name='abd'),
    path('ejercicio2/for_palabras/', views.for_palabras, name='for_palabras'),
    path('ejercicio2/while_palabra/', views.while_palabra, name='while_palabra'),
    path('ejercicio2/regresar/', views.regresar, name='regresar'),
    path('ejercicio2/whileabc/', views.whileabc, name='whileabc'),
    path('ejercicio2/whileregresa/', views.whileregresa, name='whileregresa'),

]
