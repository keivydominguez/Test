from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework .response import Response
from rest_framework.views import APIView

from .models import Producto, Tipo, Marca
from .forms import ProductoForm, MarcaForm, TipoForm
from rest_framework import serializers

#tabla de producto
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

#tabla de marca
def marca(request):
    marca_date= Marca.objects.all()

    dic_marca={
        "text": "Tabla Marca",
        "date_marca": marca_date,
    }
    return render(request, 'producto/marca.html', dic_marca)

def borrar_marca(request, id):
    tip_marca=Marca.objects.get(id=id)
    tip_marca.delete()
    return HttpResponseRedirect('/marca/')

def nuevo_marca(request):
    if request.method =="POST":
        obj_marca = MarcaForm(request.POST)
        if obj_marca.is_valid():
            mar= obj_marca.save()
        else:
            return HttpResponseRedirect('/marca/')
        return HttpResponseRedirect('/marca/')


    else:
        form_marca = MarcaForm()

        dic_marca = {
            "form_marca": form_marca
        }
        return render(request, 'producto/marcaformulario.html', dic_marca)

def editar_marca(request, id):

    if request.method =="POST":
        marca = Marca.objects.get(id=id)
        obj_marca = MarcaForm(request.POST, instance=marca)
        if obj_marca.is_valid():
            mar = obj_marca.save()
        return HttpResponseRedirect('/marca')
    else:
        marca = Marca.objects.get(id=id)
        form_marca = MarcaForm(instance=marca)

        dic_marca = {
            "form_marca": form_marca
        }
        return render(request, 'producto/marcaformulario.html', dic_marca)

#tabla tipo

def tipo(request):
    tipo = Tipo.objects.all()

    dic_tipo={
        "text": "Tabla Tipo",
        "data_tipo": tipo
    }
    return render(request, 'producto/tipo.html', dic_tipo)

def borrar_tipo(request, id):
    tipo = Tipo.objects.get(id=id)
    tipo.delete()
    return HttpResponseRedirect('/tipo/')

def nuevo_tipo(request):
    if request.method == "POST":
        obj_tipo = TipoForm(request.POST)
        if obj_tipo.is_valid():
            tip = obj_tipo.save()
        else:
            return HttpResponseRedirect('/tipo/')
        return HttpResponseRedirect('/tipo/')
    else:
        form_tipo = TipoForm()

        dic_tipo = {
            "form_tipo": form_tipo
        }
        return render(request, 'producto/tipoformulario.html', dic_tipo)

def editar_tipo(request, id):
    if request.method == "POST":
        tipo = Tipo.objects.get(id=id)
        obj_tipo = TipoForm(request.POST, instance=tipo)
        if obj_tipo.is_valid():
            tip = obj_tipo.save()
        return HttpResponseRedirect('/tipo')
    else:
        tipo = Tipo.objects.get(id=id)
        form_tipo = TipoForm(instance=tipo)

        dic_tipo = {
            "form_tipo": form_tipo
        }
        return render(request, 'producto/tipoformulario.html', dic_tipo)

#API solo muestra la id de producto
class GetProduct(APIView):
    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        producto=   Producto.objects.get(id=id)
        list = []

        list.append({
            "id": producto.id,
            "nombre": producto.nombre,
            "tipo": str (producto.tipo),
            "marca": str (producto.marca),
            "precio": producto.precio,

        })

        return Response(list)

#API aqui borramos un dato de producto
class DeletProducto(APIView):
    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        producto= Producto.objects.get(id=id)
        producto.delete()

        return Response("")

#API para agregar nuevos datos
class NuevoProducto(APIView):
    def post(self, request, *args, **kwargs):
        nombre = request.data.get("nombre")
        marca = request.data.get("marca")
        marca = Marca.objects.get(id=marca)
        tipo = request.data.get("tipo")
        tipo = Tipo.objects.get(id=tipo)
        precio = request.data.get("precio")

        producto = Producto()
        producto.nombre = nombre
        producto.marca = marca
        producto.tipo = tipo
        producto.precio = precio

        producto.save()
        return Response("")

#API muestra todo lo que hay en marca
class ListMarca(APIView):
    def post(self, request, *args, **kwargs):

        marca =Marca.objects.all()
        list=[]
        for data in marca:
            list.append(
                {
                    "id": data.id,
                    "nombre": data.marca_nombre
                }
            )
        return Response(list)

#muesta todo lo que hay en tipo
class ListTipo(APIView):
    def post(self, request, *args, **kwargs):

        tipo = Tipo.objects.all()
        list = []

        for data in tipo:
            list.append({
                "id": data.id,
                "nombre": data.tipo_nombre
            })
        return Response(list)

#API muestra todo lo que hay en producto
class VistaProducto(APIView):
    def post(self, request, *args, **kwargs):

        producto = Producto.objects.all()
        list = []

        for data in producto:
            list.append({
                "id": data.id,
                "nombre": data.nombre,
                "marca": data.marca.pk,
                "tipo": data.tipo.pk,
                "precio": data.precio
            })

        return Response(list)

class EditarProducto(APIView):
    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        nombre = request.data.get("nombre")
        marca = request.data.get("marca")
        marca = Marca.objects.get(id=marca)
        tipo = request.data.get("tipo")
        tipo = Tipo.objects.get(id=tipo)
        precio = request.data.get("precio")

        producto = Producto.objects.get(id=id)
        producto.nombre = nombre
        producto.marca = marca
        producto.tipo = tipo
        producto.precio = precio

        producto.save()
        return Response("")