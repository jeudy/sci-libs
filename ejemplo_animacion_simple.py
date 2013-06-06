# -*- coding: utf-8 -*-

# Ejemplo de animación
# Basado en http://matplotlib.org/examples/animation/random_data.html

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure("Ejemplo animacion de datos aleatorios")
ax = fig.add_subplot(111, title='xx')

# La función plot devuelve 2 objetos, por eso la , en la asignación

sp, = ax.plot([], [], 'r.')

# Seteo los limites de los ejes de 0 a 100

ax.set_ylim(0, 100)
ax.set_xlim(0, 100)

# Funcion que se llama para generar cada frame de la animación
# Recibe un parámetro i que puede ser usado como indice
# Lo que hace es actualizar los datos del plot generado arriba

def update(i):
    print "i recibido: %d" % (i)
    x = np.arange(100)
    y = np.random.randint(0, 100, 100)
    sp.set_data(x, y)
    ax.set_title('Frame dibujado: %d' % (i))
    return sp,

# Creacion de la animación, 100 frames signifca que cada 100 ms
# llama a update con un valor entre 0 y 99
# Con repeat = False hace que solo se dibujen los frames una vez
ani = animation.FuncAnimation(fig, update, frames=100, interval=100, repeat=False)
plt.show()