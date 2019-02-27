from django.urls import path

from producto.views import ProducListView
from .import views

urlpatterns = [
    path('producto/', ProducListView.as_view(), name='index'),
    path('producto/borrar/<id>', views.borrar_producto, name='borrar_producto'),
    path('producto/formulario/', views.nuevo_producto, name='nuevo_producto'),
    path('producto/editar/<id>', views.editar_producto, name='editar_producto'),
    path('get_all_products', views.GetAllProduct.as_view()),
    #path('', views.marca, name='marca'),

]