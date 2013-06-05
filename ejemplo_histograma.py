# Ejemplo sencillo de histograma con matplotlib

import numpy as np

import matplotlib.pyplot as plt

# Genera una distribución normal de 10000 números aleatorios

datos = np.random.normal(size=10000)

# Crea el histograma con 100 "espacios"

plt.hist(datos, bins=100)

plt.show()
