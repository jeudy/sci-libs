# -*- coding: UTF-8 -*-

# Ejemplo de distrbuciones del módulo stats de Scipy


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy, gamma, maxwell, norm

SAMPLE_SIZE = 100

x = np.linspace(-5,5,1000)

# Inicializo las distribuciones
cauchy_dist = cauchy()
gamma_dist = gamma(1, scale=2.)
maxwell_dist = maxwell()
norm_dist = norm()

# Calculo la funcion de densidad de probabilidad de cada distribucion

cauchy_pdf = cauchy_dist.pdf(x)
gamma_pdf = gamma_dist.pdf(x)
maxwell_pdf = maxwell_dist.pdf(x)
norm_pdf = norm_dist.pdf(x)

fig = plt.figure("Distribuciones")

sp1 = fig.add_subplot(221, title='Distribucion de Cauchy')
sp2 = fig.add_subplot(222, title='Distribucion Gamma')
sp3 = fig.add_subplot(223, title='Distribucion de Maxwell')
sp4 = fig.add_subplot(224, title='Distribucion Normal')

sp1.plot(x, cauchy_pdf, color="red")
sp2.plot(x, gamma_pdf, color="green")
sp3.plot(x, maxwell_pdf, color="blue")
sp4.plot(x, norm_pdf, color="yellow")


# Generando 100 numeros aleatorios con cada distribucion

nums_cauchy = cauchy_dist.rvs(SAMPLE_SIZE)
nums_gamma = gamma_dist.rvs(SAMPLE_SIZE)
nums_maxwell = maxwell_dist.rvs(SAMPLE_SIZE)
nums_norm = norm_dist.rvs(SAMPLE_SIZE)

fig2 = plt.figure("Muestras de numeros aleatorios")

plt.plot(nums_cauchy, 'r+')
plt.plot(nums_gamma, 'gs')
plt.plot(nums_maxwell, 'b^')
plt.plot(nums_norm, 'yo')

plt.title('Muestras de numeros aleatorios')
plt.legend(['Cauchy', 'Gamma', 'Maxwell', 'Normal'])

plt.show()