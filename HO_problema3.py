# Este programa grafica un polinomio y su derivada, y los puntos extremos
import numpy as np
import matplotlib.pyplot as pp

def p_0(x):
    return x**3+x**2-4*x+4

def p_1(x):
    return 3*x**2+2*x-4

t=np.linspace(-1,1,num=100)

pp.plot(t,p_0(t))
pp.show()

