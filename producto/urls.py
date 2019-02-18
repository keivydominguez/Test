from django.urls import path

from .import views

urlpatterns = [
    path('producto/', views.index, name='index'),
    path('producto/borrar/<id>', views.borrar_producto, name='borrar_producto'),
    #path('', views.tipo, name='tipo'),
    #path('', views.marca, name='marca'),

]