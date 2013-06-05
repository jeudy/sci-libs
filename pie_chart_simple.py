# Ejemplo casi trivial de como hacer un Pie plot

import matplotlib.pyplot as plt

valores = [10, 25, 40, 80]
colores = ['b', 'r', 'g', 'w']
etiquetas = ['A', 'B', 'C', 'D']

fig = plt.figure("Ejemplo de Pie plot")

sp1 = fig.add_subplot(111, title='Valores')

pie = sp1.pie(valores, colors=colores, labels=etiquetas)

plt.show()