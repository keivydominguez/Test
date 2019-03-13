from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime

def fecha(request):
    ejemplo = datetime.datetime(2019, 3, 4)
    ejemplo2 = datetime.datetime(2019, 8, 8)
    ejepmlo3 = datetime.datetime(2019, 12, 31)
    if request.method == "POST":
        ejemplo = request.POST.get("ejemplo")
        ejemplo= datetime.datetime.strptime(ejemplo, "%Y-%m-%d")
        diames = ejemplo.month
        diadia = ejemplo.day


       #imprime el dia de la samana
        semana = ejemplo.strftime("%A")

        #imprime el dia 366
        dia = ejemplo.strftime("%j")

        #imprime el dia de la semana
        diasemana = ejemplo.strftime("%W")

        #imprime cuandos dias falta para terminar el ciclo
        terminar = ejepmlo3 - ejemplo

        #imrpime cuandos dias falta para mi cumpleanos
        cumple = ejemplo2 - ejemplo


        #Cuando dias tiene cada mes
        dia1 = 28
        dia2 = 30
        dia3 = 31

        if int(diames) == 2:
            imprimirdia = dia1

        elif int(diames) == 4 or int(diames) == 6 or int(diames) == 9 or int(diames) == 11:
            imprimirdia = dia2

        else:
            imprimirdia=dia3

        #Cuando mes an pasado

        x = 0

        for foo in range(1, int(diames)):
            nesquepaso = foo

            if foo == 2:
                imprimirdia = dia1

            elif foo == 4 or foo == 6 or foo == 9 or foo == 11:
                imprimirdia = dia2

            else:
                imprimirdia = dia3

            x = x + imprimirdia

        x = x + diadia
    dic = {
        "bienvenido": "Bienvenido",
        "semana": semana,
        "dia": dia,
        "diasemana": diasemana,
        "termina": terminar,
        "cumple": cumple,
        "ejemplo": ejemplo,
        "imprimirdia": imprimirdia,
        "nesquepaso":  nesquepaso,
        "x": x,


    }

    return render(request, 'ejercicio2/fecha.html', dic)


def abc(request):
    abcarreglo = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z"]

    if request.method == "POST":
        abc = request.POST.get("abc")

        acomodar = ""

        for pal in abc:
            if pal == " ":
                acomodar = acomodar + " "
            else:
                x = 0
                for foo in abcarreglo:
                    if x == 24:
                        if foo == pal:
                            acomodar = acomodar + abcarreglo[0]
                    else:
                        if foo == pal:
                            acomodar = acomodar + abcarreglo[x + 1]
                    x = x + 1

    dic = {
        "text": "Bienvenido",
        "acomodar": acomodar,
    }

    return render(request, 'ejercicio2/abc.html', dic)


def regresar(request):


    abcarreglo = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z"]

    if request.method == "POST":
        regresar = request.POST.get("regresar")

        acomodar1 = ""

        for pal in regresar:
            if pal == " ":
                acomodar1 = acomodar1 + " "
            else:
                x = 0
                for foo in abcarreglo:
                    if x == 24:
                        if foo == pal:
                            acomodar1 = acomodar1 + abcarreglo[0]
                    else:
                        if foo == pal:
                            acomodar1 = acomodar1 + abcarreglo[x - 1]
                    x = x + 1


    dic = {
        "text": "Bienvenido",
        "acomodar1": acomodar1,
    }

    return render(request, 'ejercicio2/abc.html', dic)


def whileabc(request):
    abcarreglo = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z"]

    if request.method == "POST":
        abc = request.POST.get("abc")

        acomodar = ""

        pal = 0
        while pal < len(abc):
            if abc[pal] == " ":
                acomodar = acomodar + " "
            else:
                x = 0
                foo = 0
                while foo < len(abcarreglo):
                    if x == 24:
                        if abcarreglo[foo] == abc[pal]:
                            acomodar = acomodar + abcarreglo[0]
                    else:
                        if abcarreglo[foo] == abc[pal]:
                            acomodar = acomodar + abcarreglo[x + 1]
                    x = x + 1

                    foo = foo + 1

            pal = pal + 1

    dic = {
        "text": "Bienvenido",
        "acomodar": acomodar,

    }
    return render(request, 'ejercicio2/whileabc.html', dic)

def whileregresa(request):
    abcarreglo = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z"]

    if request.method == "POST":
        regresar = request.POST.get("regresar")

        acomodar1 = ""

        pal = 0
        while pal < len(regresar):
            if regresar[pal] == " ":
                acomodar1 = acomodar1 + " "
            else:
                x = 0
                foo = 0
                while foo < len(abcarreglo):
                    if x == 24:
                        if abcarreglo[foo] == regresar[pal]:
                            acomodar1 = acomodar1 + abcarreglo[0]
                    else:
                        if abcarreglo[foo] == regresar[pal]:
                            acomodar1 = acomodar1 + abcarreglo[x - 1]
                    x = x + 1

                    foo = foo + 1

            pal = pal + 1

    dic = {
        "text": "Bienvenido",
        "acomodar1": acomodar1,
    }

    return render(request, 'ejercicio2/whileabc.html', dic)



def for_palabras(request):
    aux = ""
    caja = []

    if request.method == "POST":
        letra = request.POST.get("letra")

    for i in letra:
        if i not in aux:
            aux = aux + i

    x = 0
    for a in aux :
        cont = 0
        for b in letra:
            if a == b:
                cont = cont + 1
        caja.append(cont)
    x = x + 1

    resultado = []
    v = 0
    for e in aux:
        resultado.append({
            'aux': aux[v],
            'caja': caja[v],
        })
        v = v + 1

    dic = {
        "text": "Bienvenido",
        "aux": aux,
        "caja": caja,
        "resultado": resultado,
    }

    return render(request, 'ejercicio2/for_palabras.html', dic)


def while_palabra(request):
    aux = ""
    caja = []

    if request.method == "POST":
        letra = request.POST.get("letra")

    i = 0
    while i < len(letra):
        if letra[i] not in aux:
            aux = aux + letra[i]
        i = i +1

    a = 0
    while a < len(aux):
        cont = 0
        b=0
        while b < len(letra):
            if aux[a] == letra[b]:
                cont = cont + 1
            b = b + 1
        caja.append(cont)
        a = a + 1

    resultado = []
    v = 0
    while v < len(aux):
        resultado.append({
            'aux': aux[v],
            'caja': caja[v]
        })
        v = v + 1

    dic = {
        "text": "Bienvenido",
        "aux": aux,
        "caja": caja,
        "resultado": resultado,
    }
    return render(request, 'ejercicio2/for_palabras.html', dic )