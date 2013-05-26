# -*- coding: UTF-8 -*-

# Basado en ejemplo de página 18 de SciPy and NumPy de O'Reilly

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Función f(x) = ax + b
def f(x, a, b):
    return a * x + b

# Generating clean data
x = np.linspace(0, 10, 100)
y = f(x, 1, 2)

# Adding noise to the data
yn = y + 0.9 * np.random.normal(size=len(x))

# Executing curve_fit on noisy data
popt, pcov = curve_fit(f, x, yn)

# popt contiene el estimado de a y b a partir de la regresión lineal hecha con curve_fit
# de los datos con ruido

a_estimado = popt[0]
b_estimado = popt[1]

y_estimado = f(x, a_estimado, b_estimado)

fig = plt.figure('Regresion lineal')

plt.plot(x, y, 'r')          # Valor exacto de la función
plt.plot(x, yn, 'go')   # Datos con ruido
plt.plot(x, y_estimado, 'b') # Best fit con regresioón lineal
plt.title('Regresion lineal de $f(x) = ax + b$')
plt.legend(['Verdadero', 'Ruido', 'Estimado'])
plt.show()