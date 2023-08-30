import time
t_start = time.time()
#n = 0
n = 13
#while n<1:
#    n = int(input("Ingrese un numero de elementos entero y mayor o igual a 1: "))
f = [0] * n
f[0] = 0
f[1] = 1
for i in range(2,n):
    f[i] = f[i-1]+f[i-2]
for i in range(n):
    print(f[i])
t_stop = time.time()
t_time = (t_stop - t_start)
print("time:", t_time)