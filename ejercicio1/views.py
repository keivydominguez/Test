import random

from django.shortcuts import render
from random import randrange
from .models import Numero

# Create your views here.

def holamundo(request):


    list = []
    for i in range(10):
        num = random.randint(0, 100)
        status=""
        if num % 2 == 0:
           status="si"
        else:
           status="no"

        list.append({
            "numero": num,
            "status": status,
        })

    dic ={
        "text": "HOLA MUNDO",
        "list": list,
    }

    return render(request, 'ejercico1/holamundo.html', dic)

def numero_medio(resquets):
    if resquets.method == "POST":
        obj_numero =


    if request.method == "POST":
        obj_producto = ProductoForm(request.POST)
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

        dic = {

            "form_producto_dic": form_producto
        }
    return render(request, 'producto/formulario.html', dic)