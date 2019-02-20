from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Producto, Tipo, Marca
from .forms import ProductoForm


def index(request):
    # aqui llamas a los produstors query
    productos = Producto.objects.all()
    #select * from productos

    # aqui los recorres xon un for
    # list = []
    #
    # for data in productos:
    #
    #     list.append({
    #         "id": data.id,
    #         "nombre": data.nombre,
    #         "tipo": data.tipo,
    #         "marca": data.marca,
    #         "precio": data.precio,
    #     })

    # aqui van las listas


    ctx= {
        "texto": "producto y tipo",
        "lista": productos,
    }
    return render(request, 'producto/producto.html', ctx)

def borrar_producto(request, id):
    Pro_borrar = Producto.objects.get(id=id)
    Pro_borrar.delete()
    return HttpResponseRedirect('/producto/')

def nuevo_producto(request):

    if request.method == "POST":
        obj_producto= ProductoForm(request.POST)
        if obj_producto.is_valid():
            pro = obj_producto.save()
        else:
            print("error")
            return HttpResponseRedirect('/producto/')

        # name=   request.POST.get('name')
        # marca=  request.POST.get('marca')
        # tipo=   request.POST.get('tipo')
        # precio= request.POST.get('precio')
        # obj_marca = Marca.objects.get(id=marca)
        # obj_tipo = Tipo.objects.get(id=tipo)
        #
        # p = Producto(nombre=name, marca=obj_marca, tipo=obj_tipo, precio=precio)
        # p.save()

        return HttpResponseRedirect('/producto/')

    else:
        form_producto = ProductoForm()

        dic={

            "form_producto_dic": form_producto
        }
    return render(request, 'producto/formulario.html', dic)

def editar_producto(request, id):
    if request.method == "POST":
        producto=Producto.objects.get(id=id)
        obj_producto= ProductoForm(request.POST, instance=producto)
        if obj_producto.is_valid():
            pro=obj_producto.save()
        return HttpResponseRedirect('/producto/')

    else:
        producto= Producto.objects.get(id=id)
        form_producto = ProductoForm(instance=producto)

        dic = {

            "form_producto_dic": form_producto
        }
        return render(request, 'producto/formulario.html', dic)

class GetAllProduct(APIView):
    def post(self, request, *args, **kwargs):
        productos = Producto.objects.all()
        list = []

        for data in productos:

            list.append({
                "id": data.id,
                "nombre": data.nombre,
                "tipo": str(data.tipo),
                "marca": str(data.marca),
                "precio": data.precio,
            })

        return Response(list)