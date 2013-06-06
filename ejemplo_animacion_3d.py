# -*- coding: utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure("Ejemplo de animacion 3D")

# Se define un eje como proyección 3D

ax = plt.axes(projection='3d')

z = np.random.rand(100)
x = np.random.rand(100)
y = np.random.rand(100)

sp, = ax.plot(x, y, z, 'r.')

def update(i):
    z = np.random.rand(100)
    x = np.random.rand(100)
    y = np.random.rand(100)
    sp.set_data(x, y)
    sp.set_3d_properties(z)
    return sp,

# Creacion de la animación, 100 frames signifca que cada 100 ms
# llama a update con un valor entre 0 y 99
# Con repeat = False hace que solo se dibujen los frames una vez
ani = animation.FuncAnimation(fig, update, frames=100, interval=100, repeat=False)
plt.show()

