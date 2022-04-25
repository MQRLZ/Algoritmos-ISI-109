# Ej 12 condicionalitos
# Variables = N1, N2, N3, N4, N5, N6 -> Reales

N1 = float(input("Ingrese 6 números positivos diferentes. "))
N2 = float(input())
N3 = float(input())
N4 = float(input())
N5 = float(input())
N6 = float(input())

if N1 != N2 and N2 != N3 and N3 != N4 and N4 != N5 and N5 != N6 and N1 > 0 and N2 > 0 and N3 > 0 and N4 > 0 and N5 > 0 and N6 > 0:

    if N6 > N5 and N6 > N4 and N6 > N3 and N6 > N2 and N6 > N1:
        print(N6)
    elif N5 > N6 and N5 > N4 and N5 > N3 and N5 > N2 and N5 > N1:
        print(N5)
    elif N4 > N6 and N4 > N5 and N4 > N3 and N4 > N2 and N4 > N1:
        print(N4)
    elif N3 > N6 and N3 > N5 and N3 > N4 and N3 > N2 and N3 > N1:
        print(N3)
    elif N2 > N6 and N2 > N5 and N2 > N4 and N2 > N3 and N2 > N1:
        print(N2)
    elif N1 > N6 and N1 > N5 and N1 > N4 and N1 > N3 and N1 > N2:
        print(N1)
    else:
        print("ayuda me rompi")

else:
    print("Pibe no son diferentes.")