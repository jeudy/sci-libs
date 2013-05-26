# -*- coding: UTF-8 -*-

import numpy as np
from scipy.integrate import quad


# Funcion a integrar: cos²(e^x)
def f(x):
    return np.cos(np.exp(x)) ** 2

# Integrar la función en los límites 0, 3
# quad devuelve un arreglo con 2 elementos: el primero, la solución
# el segundo, el error
solucion = quad(f, 0, 3)

print "La solución es: %s " % (str(solucion))