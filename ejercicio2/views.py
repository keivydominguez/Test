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

