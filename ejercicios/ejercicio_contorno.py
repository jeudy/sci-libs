import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# El archivo que se carga tiene formato X,Y,Z,VX,VY,VZ,D,Masa,RHO

RUTA_ENTRADA = './data/posiciones.csv'

archivo = open(RUTA_ENTRADA, 'r')

# Consume el header
linea = archivo.readline()

# Lee la primera linea
linea = archivo.readline()

lista_valores = []

while linea:
    valores = np.fromstring(linea, sep=',')
    lista_valores.append(valores)
    linea = archivo.readline()

archivo.close()

lista_valores_np = np.array(lista_valores)

x = lista_valores_np[:, 0]
y = lista_valores_np[:, 1]
densidad = lista_valores_np[:, 8]

mx = interp1d([x.min(), x.max()], [0, 1])
my = interp1d([y.min(), y.max()], [0, 1])
md = interp1d([densidad.min(), densidad.max()], [0, 255])

x = np.array(map(mx, x))
y = np.array(map(my, y))
densidad = np.array(map(md, densidad))

# X = np.array([x, y, densidad]).reshape(len(x), 3)

X = np.array([x, y]).reshape(len(x), 2)


fig = plt.figure("Plot de contorno de densidad")

sp1 = fig.add_subplot(111, title='Plano xy')

im = sp1.imshow(X, cmap=plt.cm.jet)

fig.colorbar(im, ax=sp1)

plt.show()

# normal = [[1,2,3], [4,5,6], [7,8,9]]
# npnormal = np.array(normal)

# Jalar columnas X, Y y rho:

# npnormal[0,:], npnormal[1,:], etc

# Con eso se construye el plot
