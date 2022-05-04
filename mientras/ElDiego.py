# ejercicios liberales



# variables: ventas, tacaro -> int; ventas, promedio -> float
def ej2():
    ventas = 0
    promedio = 0
    tacaro = 0
    factura = float(input("Ingrese la factura pibe: "))

    while factura != 0:
        ventas = ventas + 1
        promedio = promedio + factura
        if factura > 30:
            tacaro = tacaro + 1
        factura = float(input("Ingrese la factura pibe: "))

    print(f"Se realizaron {ventas} ventas, con un promedio de {promedio / ventas} y los importes que superan los 30 pesos fueron {tacaro}.")

# variables: alumno, promedio, comisiones -> int; parcial -> float
def ej10():

    comisiones = int(input("Decime las comisiones grax "))

    for i in range(1, comisiones + 1):
        alumno = 0
        promedio = 0
        parcial = float(input("Nota del parcialito grax "))
        while parcial != 0:
            alumno += 1
            promedio = promedio + parcial
            parcial = float(input("Nota del parcialito grax "))
        print(f"La comisión {i} tiene un promedio de notas de {promedio / alumno}")
        
def ej11():

    dia = int(input("ingresame el dia "))
    laburantes = int(input("cuántos laburaron? "))
    diastotales = 0
    while dia != 0:
        horasanteriores = 0
        esteeselpibe = 0
        esteessupromedio = 0
        horastrabajadas = 0
        for pibe in range(1, laburantes + 1):
            doxxeado = int(input("doxxealo al pibe que labura "))
            horas = int(input("cuánto laburó? "))
            horastrabajadas = horastrabajadas + horas
            cantlaburante += 1
            if (horas > horasanteriores):
                esteeselpibe = doxxeado
                esteessupromedio = horas / laburantes
        dia = int(input("ingresame el dia "))
        diastotales += 1
        print(f"El empleado más piola después de {diastotales} días es {esteeselpibe}.")
        print(f"Hubo un promedio de {esteessupromedio} horas trabajadas entre todos.")
    print(f"Se trabajó un total de {horastrabajadas} horas.")

    

ej11()
            