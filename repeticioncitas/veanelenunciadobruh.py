# Ej 10 for
# Variables = n1, n2 -> int

n1 = int(input("ingresame los numeritos "))
n2 = int(input())

listita = []

if (n1 < 0 or n2 < 0):
    print("ingresame numeros naturales porfa")

elif (n1 < n2):
    n1 = n1 - 1
    for c in range(n1, n2):
        n1 = n1 + 1
        listita.append(n1)
    print(listita)

else:
    print("perdoname pa no te puedo mostrar nada.")