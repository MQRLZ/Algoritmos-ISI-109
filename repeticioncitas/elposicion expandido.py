# Ej 17 for
# Variables: max, pos, nro -> int
nro = int(input("Ingresar Numerito: "))

max = nro
min = nro
posmax = 1
posmin = 1

for I in range(2, 93):
    nro = int(input("Ingresar Numerito: "))
    if nro > max:
        max = nro
        posmax = I
    
    elif nro < min:
        min = nro
        posmin = I

print(f"El mayor número fue {max} en la posición {posmax} y el menor fue {min} en la posición {posmin}")