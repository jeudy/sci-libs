# -*- coding: utf-8 -*-

# Ejemplo sencillo de histograma con matplotlib

import numpy as np
import matplotlib.pyplot as plt

SIZE_POBLACION = 100000

# Simulación de edades de una población, entre 1 y 85 años

edades = np.random.random_integers(1,85,SIZE_POBLACION)

# Vamos a sacar el conteo de personas dentro de diferentes rango de edad
# de 1 a 10, de 11 a 17, de 18 a 30, de 31 a 50 y mayor a 50

rango_1_10 = edades[(edades>=1) & (edades <= 10)].size
rango_11_17 = edades[(edades>=11) & (edades <= 17)].size
rango_18_30 = edades[(edades>=18) & (edades <= 30)].size
rango_31_50 = edades[(edades>=31) & (edades <= 50)].size
rango_51 = edades[edades>=51].size

rangos = [rango_1_10, rango_11_17, rango_18_30, rango_31_50, rango_51]
colores = ['b', 'r', 'g', 'y', 'w']
etiquetas = ['De 1 a 10', 'De 11 a 17', 'De 18 a 30', 'De 31 a 50', 'Mas de 51']

fig = plt.figure("Rangos de edad en poblacion")

sp1 = fig.add_subplot(111, title='Edades')

pie = sp1.pie(rangos, colors=colores, labels=etiquetas, explode=(0,0,0,0,0.05))

plt.show()