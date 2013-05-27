# -*- coding: UTF-8 -*-

# Ejemplo de resolución de sistemas de ecuaciones lineales con scipy
# Sistema de ecuaciones está dado por:
# x  + 3y + 5z = 10
# 2x + 5y + z  =  8
# 2x + 3y + 8z =  3

import numpy as np
from scipy import linalg

matriz_coeficientes = np.array(
    [[1, 3, 5],
    [2, 5, 1],
    [2, 3, 8]]
)

vector_lado_derecho = np.array([10., 8., 3.])

soluciones = linalg.solve(matriz_coeficientes, vector_lado_derecho)

print "Solucion al sistema: %s" % (soluciones)

# Probamos que la solucion sea la correcta, multiplicando la matriz de coeficientes por
# la solucion, debemos obtener el vector de lado derecho

prueba = matriz_coeficientes.dot(soluciones)

print "Probando las soluciones: %s." % (prueba)