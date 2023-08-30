n=0
while(n<1):
    n = int(input("Ingrese un numero natural: "))
x = [7,5,9]
min = x[0]
max = x[0]

for i in range(1, n):
    if(x[i]<min):
        min = x[i]
    if(x[i]>max):
        max = x[i]

media = 0
for i in range(n):
    media += x[i]
media /= n

varianza = 0
for i in range(n):
    varianza += (x[i]-media)**2
varianza /= (n-1)
print("media =", media)
print("varianza =", varianza)
print("min =", min)
print("max =", max)