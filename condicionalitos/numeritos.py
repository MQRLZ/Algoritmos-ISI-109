# Ej 4 condicionalitos
# Variables = N1, N2, N3 -> Enteros

N1 = int(input("Ingrese 3 números enteros en orden creciente: "))
N2 = int(input())
N3 = int(input())

if N1 < N2 and N2 < N3:
    print("Están ingresados en orden creciente.")

else:
    print("No están en orden creciente.")