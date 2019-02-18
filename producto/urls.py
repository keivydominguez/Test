from django.urls import path

from .import views

urlpatterns = [
    path('producto/', views.index, name='index'),
    #path('', views.producto,name='producto'),
    #path('', views.tipo, name='tipo'),
    #path('', views.marca, name='marca'),

]