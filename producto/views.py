from django.shortcuts import render
from django.http import HttpResponse

from .models import Producto


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
