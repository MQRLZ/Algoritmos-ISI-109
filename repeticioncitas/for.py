# Ej 1 for
# Variables: remu, horas -> int
# Constante: empleados -> int

remu = int(input("Especificar la remuneración: "))

for empleados in range(50):
    horas = int(input(f"Ingresar las horas trabajadas del empleado {empleados}: "))
    def calcularsueldo():
        return remu * horas
    print(f"El sueldo de este empleado es {calcularsueldo()}")