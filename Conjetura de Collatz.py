reg = True
while reg:
    n = int(input("Ingrese un numero entero mayor que 1: "))
    if (n>1):
        reg = False
contador = 0
cont = 1
maximo = 0
print(n)
while(n > 1):
    if (n>maximo):
        maximo = n
    if (n%2)==0:
        n = n/2
    else:
        n = (n*3)+1
    print(n)
    contador += 1
    cont +=1
print("Se han hecho", contador, "iteraciones")
print("Hay", cont, "terminos")
print("Maximo =", maximo)