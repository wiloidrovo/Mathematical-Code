import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a:
    dis = (b*b) - (4*a*c)
    r_dis = math.sqrt(abs(dis))
    if (dis >= 0):
        x_1 = (-b + r_dis)/(2*a)
        x_2 = (-b - r_dis)/(2*a)
        print ("x1 =", x_1, "x2 =", x_2)
    else:
        x_1r = -b/(2*a)
        x_1i = r_dis/(2*a)
        print("x1 =", x_1r, "+", abs(x_1i), "i")
        print("x2 =", x_1r, "-", abs(x_1i), "i")
else:
    print("Error")