# -*- coding: UTF-8 -*-

import numpy as np
from scipy.integrate import quad, Inf


# Funcion a integrar: cos²(e^x)
def f(x):
    return np.exp(x)

# Integrar la función en los límites 0, 3
# quad devuelve un arreglo con 2 elementos: el primero, la solución
# el segundo, el error
solucion = quad(f, -Inf, 0)

print "La solución es: %s " % (str(solucion))
