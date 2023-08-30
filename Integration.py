# Inputs: 
#   a, b: float (integration limits)
#   fx: function
# Outputs:
#   fint: float (Aproximation to integral fx)
# Procedure: 
#   Rectangles method
#  
from sympy import * # python symbolic module

go = True
fx = input('Function f(x): ')
try:
    a = float(input('Lower limit: '))
    b = float(input('Upper limit: '))
    n = int(input('n: '))
    if (a > b) or (n < 1):
        print('Invalid range or number of chunks')
        go = False
except:
    print('Invalid Data')
    go = False
try:
    x = Symbol('x')
    thefun = sympify(fx, evaluate=False)
    va = thefun.evalf(subs={x:a}) #eval(fx, {'x': a})
    vb = thefun.evalf(subs={x:b}) #eval(fx, {'x': b})
except:
    print('Invalid function f(x)')
    go = False
if go:
    # This function calculates the definite integral of fx with limits (a,b)  
    freal = integrate(thefun, (x, a, b))
    fint = 0
    xint = a
    h = (b-a)/n
    for i in range(0,n):
        fint += thefun.evalf(subs={x:xint}) #eval(fx, {'x': x})
        xint += h
    fint *= h
    print('Aprox: ', fint)
    print('Exact: ', freal)