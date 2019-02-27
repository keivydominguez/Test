import random

from django.shortcuts import render
from random import randrange

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