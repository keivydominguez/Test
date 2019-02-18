from django.urls import path

from .import views

urlpatterns = [
    path('producto/', views.index, name='index'),
    path('producto/borrar/<id>', views.borrar_producto, name='borrar_producto'),
    path('producto/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    #path('', views.marca, name='marca'),

]