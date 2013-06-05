import pylab as pl

RUTA_ENTRADA = './data/posiciones.csv'
RUTA_SALIDA = './data/posiciones_numpy.csv'

archivo = open(RUTA_ENTRADA, 'r')
salida = open(RUTA_SALIDA, 'w')

linea = archivo.readline()
linea = archivo.readline()
while linea:
    valores = linea.split(',')
    salida.write(",".join(valores[0:3]))
    salida.write(",")
    linea = archivo.readline()

archivo.close()
salida.close()

posiciones = pl.fromfile(RUTA_SALIDA, sep=',').reshape(5000,3)  # Acomodo los datos en un arreglo 5000x3

x = posiciones[:,0]
y = posiciones[:,1]
z = posiciones[:,2]

fig = pl.figure("Cumulo estelar")

sp1 = fig.add_subplot(131, title='Plano xy')
sp2 = fig.add_subplot(132, title='Plano xz')
sp3 = fig.add_subplot(133, title='Plano yz')

sp1.plot(x, y, 'ro')
sp2.plot(x, z, 'g+')
sp3.plot(y, z, 'bs')

# Al invocar a figure, reseteamos para poder dibujar mas figuras

pl.figure("Plano XY")

pl.scatter(x,y)

pl.figure("Plano XZ")

pl.scatter(x,z)

pl.figure("Plano YZ")

pl.scatter(y,z)

pl.show()
