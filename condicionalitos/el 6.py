# Ej 6 condicionalitos
# Variables = A, B, C -> string

#A = str(input("Ingrese tres letras mayúsculas. "))
#B = str(input())
#C = str(input()) 

#letritas = [A, B, C]

#if A < B and B < C: 
#    print(letritas)

#else:
#    letritas.sort()
#    print(letritas)

a = str(input("Ingrese tres letras mayúsculas. "))
b = str(input())
c = str(input()) 

if a != b and a != c and b != c:
    if a < b and b < c:
        print(a,b,c)
    elif b < a and a < c:
        print(b,a,c)
    elif c < b and b < a:
        print(c,b,a)
    elif a < c and c < b:
        print(a,c,b)
    elif b < c and c < a:
        print(b,c,a)
    else:
        print(c,a,b)
else:
    print("No pueden ser iguales pa.")     