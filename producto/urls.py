from django.urls import path

from .import views

urlpatterns = [
    path('producto/', views.index, name='index'),
    path('producto/borrar/<id>', views.borrar_producto, name='borrar_producto'),
    path('producto/formulario/', views.nuevo_producto, name='nuevo_producto'),
    path('producto/editar/<id>', views.editar_producto, name='editar_producto'),
    path('get_all_products', views.GetAllProduct.as_view()),

    path('marca/', views.marca, name='marca_principal'),
    path('marca/borrar/<id>', views.borrar_marca, name='marca_tipo'),
    path('marca/formulario/', views.nuevo_marca, name='nuevo_marca'),
    path('marca/editar/<id>', views.editar_marca, name='editar_marca'),
    #path('', views.marca, name='marca'),

]