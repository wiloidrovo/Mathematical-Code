import time
import math
#t_start = time.process_time()
t_start = time.time()
#n = 0
n = 13
X = []
#while n<1:
#    n = int(input("Ingrese un numero de elementos entero y mayor o igual a 1: "))
sqrt_5 = math.sqrt(5)
phi = (1 + sqrt_5) / 2
psi = (1 - sqrt_5) / 2
for i in range(n):
    Fn = (1 / sqrt_5) * (phi**i - psi**i)
    X.append(Fn)
print(X)
#t_stop = time.process_time()
t_stop = time.time()
t_time = (t_stop - t_start)
print("time:", t_time)