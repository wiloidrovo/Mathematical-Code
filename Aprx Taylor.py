# Aproximacion a sin(x) por Taylor.
# Ejercicio 2 de MidTerm.
x = float(input("x = "))
n = -1
while(n<0):
    n = int(input("n = "))
aprox = 0
signo = 1
potx = x
fact = 1
for i in range(n+1):
    val = 2*i+1
    if (val>1):
        fact *= (val)*(val-1)
    aprox += (signo * potx)/fact
    signo *= (-1)
    potx *= (x**2)
print(aprox)