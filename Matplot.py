import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def h(x):
    return np.cos(x)

x = np.linspace(0,10,500)
plt.plot(x,f(x),"r--",label="seno")
plt.plot(x,h(x),label="coseno")
plt.title("Funciones Trigonometricas")
plt.legend()
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.grid()
plt.show()