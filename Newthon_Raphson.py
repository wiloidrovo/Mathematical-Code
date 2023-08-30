# Método de Newton Raphson para hallar la raíz de una función
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Función
x = sp.Symbol("x")
f = sp.sympify(input("Ingrese una funcion f(x): "))  # cos(x)-x**3
f_num = sp.lambdify(x, f)

# Derivada
dx = sp.diff(f,x)
print("Su derivada es:", dx)
dx_num = sp.lambdify(x, dx)

# La derivada es cero en:
print("La derivada es cero en x =", sp.solve(dx,x))

a = float(input("Ingrese el punto inicial: "))  # 3.141592

tolerancia = 0.0000001

xi = a
error = 1
print("Aproximaciones:")
contador = 0
while(error >= tolerancia):
    try:
        xi_1 = xi - (f_num(xi)/dx_num(xi))
        error = abs((xi_1 - xi)/xi_1)
        xi = xi_1
        contador+=1
        subindice = chr(8320 + contador)
        print("x"+ subindice+ "=", xi)
    except ZeroDivisionError:
        print("Error: División por cero en xi =", xi)
        break

if error < tolerancia:
    print("La raiz de (" + str(f) + ") es =", xi)

    # Gráfica de las funciones
    x_values = np.linspace(xi-2,xi+2,500)
    plt.axhline(y=0,color='grey',linestyle='--')
    plt.plot(x_values,f_num(x_values),"blue",label="funcion original")
    plt.plot(x_values,dx_num(x_values),"red",linestyle='--',label="funcion derivada")
    plt.plot(xi,f_num(xi),"black",marker ="o",label="raiz")
    plt.title("Calculo de raices")
    plt.legend()
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.grid()
    plt.show()