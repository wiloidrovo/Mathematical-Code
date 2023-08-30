n = int(input("Ingrese un numero mayor que 1: "))
suma = 1
for i in range(2, n-1):
    if n%i == 0:
        suma+=i
if (suma==n):
    print(n, "es un numero perfecto")