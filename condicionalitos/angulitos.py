# Ej 3 condicionalitos
# Variables: A1, A2, A3 -> Reales

A1 = float(input("Ingrese ángulo A "))
A2 = float(input("Ingrese ángulo B "))
A3 = float(input("Ingrese ángulo C "))

if A1 + A2 + A3 == 180:
    if (A1 == 90 or A2 == 90 or A3 == 90) and (A1 > 0 and A2 > 0 and A3 > 0):
        print("El tríangulo es rectángulo.") 

    else:
        print("El tríangulo no es rectángulo.")

else: 
    print("No es un triángulo.")
