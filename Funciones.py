def myread():
    a = 0
    b = 0
    while (a >= b):
        a = int(input("Ingrese un número natural: "))
        b = int(input("Ingrese un número natural mayor al anterior: "))
    return a,b

def calcprob(v1, v2):
    comb = fact(v2)/(fact(v2-v1)*fact(v1))
    return 1/comb

def fact(n):
    f = 1
    for i in range(1,n):
        f = f*i
    return f

"""
def readArray(n):
    X = []
    for i in range(n):
        val = float(input("valor", i))
        X.append(val)
    return X
"""

m,n = myread()
prob = calcprob(n,m)
print(prob)