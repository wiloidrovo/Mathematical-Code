n = int(input("Ingrese un numero natural: "))
suma = 0
for i in range (1, n+1):
    print(i)
    suma += i
print("Suma =", suma)

mult = 1
for i in range(1, n+1):
    mult *= i
print("Multiplicación =", mult)