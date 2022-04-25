# Ej 2 while
# variables: ventas, tacaro -> int; ventas, promedio -> float

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