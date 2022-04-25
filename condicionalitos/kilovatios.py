# Ej 11 condicionalitos
# Variables = kilov -> Real

kilov = float(input("Ingrese los kilovatios consumidos. "))

if kilov <= 200:
    print(f"Consumiste: ${kilov * 0.05}")

elif 200 < kilov < 1000:
    print(f"Consumiste:  ${kilov * 0.1}")

elif kilov >= 1000:
    print(f"Consumiste: ${kilov * 0.15}")