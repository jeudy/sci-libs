# -*- coding: utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure("Ejemplo de plot 3D")

# Se define un eje como proyección 3D

ax = plt.axes(projection='3d')

z =  np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)

# Cambiar datos x,y,z por np.random.rand(100)

#Puede ser .plot en lugar de scatter

ax.scatter(x, y, z)

plt.show()