# Ej 1 condicionalitos
# Variables: N1 y N2 -> Reales

N1 = float(input("Ingrese un numero real: "))
N2 = float(input("Ingrese otro numero real: "))

if N1 == N2:
    print("Dale flaco no rompas las bolas tienen que ser distintos")
    
elif N1 > N2:
    print(f"De manera ordenada serian: {N2}, {N1}")

else:
    print(f"De manera ordenada serian: {N1}, {N2}")
