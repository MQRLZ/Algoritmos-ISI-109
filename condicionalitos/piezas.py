# Ej 7 condicionalitos
# Variables = tipo -> string, medida -> float

tipo = str(input("Ingrese el tipo A o B: "))

if tipo == "A":
    medida = float(input("Ingrese la medida de la pieza: "))
    if medida>1.63 and medida<1.67:
        print("La pieza es de calidad pibe.")
    else:
        print("Ta mal pibe.")

elif tipo == "B":
    medida = float(input("Ingrese la medida de la pieza: "))
    if medida>1.77 and medida<1.83:
        print("La pieza es de calidad pibe.")
    else:
        print("Ta mal pibe.")
        
else:
    print("Ta mal el tipo pibe, volvelo a intentar vos podés.")