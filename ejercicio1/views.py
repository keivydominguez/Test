import random

from django.shortcuts import render
from random import randrange
from .models import Numero
from .forms import NumeroForm
from django.http import HttpResponse, HttpResponseRedirect

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

def numero_medio(request):
    if request.method == "POST":
        num1 =request.POST.get('numero1')
        num2 =request.POST.get('numero2')
        num3 =request.POST.get('numero3')

    if num1 <= num2:

        if num2 <= num3:
            medio = num2
        else:
            num3 <= num1
            medio = num3
    else:

        medio = num1

    dic = {

        "mediano": medio,

    }
    return render(request, 'ejercico1/formulario.html', dic)
