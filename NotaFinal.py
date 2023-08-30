vn = False
vp = False
nd = 0
sp = 0

for i in range(1, 5):
    n = float(input("Ingrese la nota: "))
    p = float(input("Ingrese su porcentaje: "))

    sp += +p
    nd += (n*p/100)
    if (n<0) or (n>10):
        vn = True
    if (p<0):
        vp = True
if sp != 100:
    vp = True
if vp or vn:
    print("Error")
else:
    print("Su nota total es:", nd)