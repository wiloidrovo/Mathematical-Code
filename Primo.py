go = True
while go:
    n = int(input("Ingrese un numero: "))
    if n>0:
        go = False
unidades = n%10
decenas = n//10
for i in range(2, n):
    num_div = 0
    for j in range(1, i + 1):
        if i % j == 0:
            num_div += 1
    if num_div == 2:
        h = str(i)
        k = str(n)
        digitos_coinciden = False
        for l in k:
            if l in h:
                digitos_coinciden = True
                break
        if not digitos_coinciden:
            print(i)