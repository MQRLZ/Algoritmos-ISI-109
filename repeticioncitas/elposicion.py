# Ej 16 for
# Variables: max, pos, nro -> int
nro = int(input("Ingresar Numerito: "))

max = nro
pos = 1

for I in range(2, 93):
    nro = int(input("Ingresar Numerito: "))
    if nro > max:
        max = nro
        pos = I

print(f"El mayor número fue {max} en la posición {pos}.")