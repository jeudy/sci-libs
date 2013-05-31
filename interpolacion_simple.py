# -*- coding: UTF-8 -*-

# Ejemplo de interpolación simple con SciPy
# Basado en ejemplo de página 22 de SciPy and NumPy de O'Reilly

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0, 10 * np.pi, 20)      # Se crea el espacio lineal con 20 puntos
y = np.cos(x)                           # Se obtienen los datos para los 20 puntos

# Se realiza la interpolación con 2 métodos diferentes, se obtienen
# 2 funciones fl y fq con las que podemos estimar los valores para
# más puntos dentro del rango del espacio lineal

fl = interp1d(x, y, kind='linear')
fq = interp1d(x, y, kind='quadratic')
# x.min and x.max are used to make sure we do not
# go beyond the boundaries of the data for the
# interpolation.
xint = np.linspace(0, 10 * np.pi, 1000)  # Se crea un nuevo espacio, mismo rango, pero mas puntos
yintl = fl(xint)
yintq = fq(xint)
yreal = np.cos(xint)

plt.figure("Interpolacion1")
plt.plot(x, y, 'ro')          # Muestras
plt.plot(xint, yintl, 'g')   # Interpolación lineal
plt.plot(xint, yreal, 'b')   # Datos reales
plt.title('Interpolacion lineal de $f(x) = cos(x)$')
plt.ylim(-1.5, 1.5)
plt.legend(['Muestra', 'Interpolacion', 'Valor real'])

plt.figure("Interpolacion2")
plt.plot(x, y, 'ro')          # Muestras
plt.plot(xint, yreal, 'b')   # Datos reales
plt.plot(xint, yintq, 'g')   # Interpolación cuadrática
plt.title('Interpolacion cuadratica de $f(x) = cos(x)$')
plt.legend(['Muestra', 'Interpolacion', 'Valor real'])
plt.ylim(-1.5, 1.5)

plt.show()