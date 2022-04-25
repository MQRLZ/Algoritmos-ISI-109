# Ej 4 for
# Variables: numero, sumanumeros -> int
# Constantes: C -> int

sumanumeros = 0

for C in range(200):
    numero = int(input("Ingrese un numero entero: "))
    sumanumeros += numero

print(f"La suma es {sumanumeros}.")