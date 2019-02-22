from django.urls import path

from .import views

urlpatterns = [
    path('producto/', views.index, name='index'),
    path('producto/borrar/<id>', views.borrar_producto, name='borrar_producto'),
    path('producto/formulario/', views.nuevo_producto, name='nuevo_producto'),
    path('producto/editar/<id>', views.editar_producto, name='editar_producto'),
    path('get_all_products', views.GetAllProduct.as_view()),
    #ESta API muestra solo la id de producto
    path('get_produtc', views.GetProduct.as_view()),
    #Esta API borra un solo dato
    path('delet_producto', views.DeletProducto.as_view()),
    #ESta API agrega nuevos datos
    path('nuevo_producto', views.NuevoProducto.as_view()),
    #Esta API muestra todo los datos que estan en marca
    path('list_marca', views.ListMarca.as_view()),
    #ESta API meusta todo los datos que tiene tipo
    path('list_tipo', views.ListTipo.as_view()),
    #ESta API muesta todo lo que tiene proeducto
    path('vista_producto', views.VistaProducto.as_view()),
    #ESta API edita todo lkos datos de producto
    path('editar_producto', views.EditarProducto.as_view()),


    path('marca/', views.marca, name='marca_principal'),
    path('marca/borrar/<id>', views.borrar_marca, name='marca_tipo'),
    path('marca/formulario/', views.nuevo_marca, name='nuevo_marca'),
    path('marca/editar/<id>', views.editar_marca, name='editar_marca'),

    path('tipo/', views.tipo, name='tipo_principal'),
    path('tipo/borrar/<id>', views.borrar_tipo, name='borrar_tipo'),
    path('tipo/formulario/', views.nuevo_tipo, name='nuevo_tipo'),
    path('tipo/editar/<id>', views.editar_tipo, name='editar_tipo'),

    #path('', views.marca, name='marca'),

]