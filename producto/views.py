from django.shortcuts import render
from django.http import HttpResponse

from .models import Producto


def index(request):
    # aqui llamas a los produstors query
    productos = Producto.objects.all()

    # aqui los recorres xon un for

    for producto in productos:
        print(producto)

    # aqui van las listas



    ctx= {
        "texto": "producto y tipo"
    }
    return render(request, 'producto/producto.html', ctx)
