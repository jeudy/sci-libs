# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def b(m, x, y):
    return y - m*x

def graficar_derivada(punto):
    m = df(punto)
    y_punto = f(punto)
    x_tangente = np.linspace(punto - 1, punto + 1, 100)
    y_tangente = (m*x_tangente) + b(m, punto, y_punto)
    plt.plot(x_tangente, y_tangente, 'g')

f = np.poly1d([2, 5, 0, -2])

df = f.deriv()

x = np.linspace(-3., 3., 1000)

ys = f(x)
dy = df(x)

plt.figure("Graficando funciones y su derivada")

plt.title("$f(x) = 2x^3 + 5x^2 - 2$ y $f'(x)$ en x = -2, -0.5 y 1.5")
plt.plot(x, ys, 'r')

graficar_derivada(-2)
graficar_derivada(-0.5)
graficar_derivada(1.5)
# ---
puntos = [-2, -0.5, 1.5]
plt.plot(puntos, f(puntos), 'bo')
plt.show()