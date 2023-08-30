import math
x = float(input("Ingrese el valor: "))
parte_entera = math.trunc(x)
parte_decimal = math.trunc((x-parte_entera)*100)

b100 = (parte_entera//100)
resto = (parte_entera%100)
b50 = (resto//50)
resto = (resto%50)
b20 = (resto//20)
resto = (resto%20)
b10 = (resto//10)
resto = (resto%10)
b5 = (resto//5)
resto = (resto%5)

parte_decimal += (resto*100)

m50 = (parte_decimal//50)
resto = (parte_decimal%50)
m25 = (resto//25)
resto = (resto%25)
m10 = (resto//10)
resto = (resto%10)
m5 = (resto//5)
resto = (resto%5)
m1 = (resto//1)

print("Billetes de 100:", b100, "Billetes de 50:", b50, "Billetes de 20:", b20,
      "Billetes de 10:", b10, "Billetes de 5:", b5)
print("Monedas de 50:", m50, "Monedas de 25:", m25, "Monedas de 10:", m10, "Monedas de 5:", m5,
      "Monedas de 1:", m1)