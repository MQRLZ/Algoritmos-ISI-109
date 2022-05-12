# Ej 1 Globalizador
# Legajo, ParcialesAprobados -> int; Nota -> Float


def INGRESARNOTA():
    global ParcialesAprobados, legajo, Nota
    ParcialesAprobados = 0
    for Parciales in range(1, 6):
        Nota = float(input(f"Ingresar resultado del parcial Nº {Parciales}: "))
        if Nota > 5:
            ParcialesAprobados += 1

def PROGRAMA():
    global Nota, legajo, ParcialesAprobados
    Nota = 0
    legajo = int(input("Ingresar legajo del alumno. Ingresar 0 para finalizar: "))

    while legajo != 0:
        INGRESARNOTA()
        if ParcialesAprobados > 4:
            print("Regular")
        elif ParcialesAprobados == 3:
            print("A recuperatorio")
        elif ParcialesAprobados < 3:
            print("A recursar")
        legajo = int(input("Ingresar legajo del alumno. Ingresar 0 para finalizar: "))

    print("Fin del programa.")
    
PROGRAMA()
   

