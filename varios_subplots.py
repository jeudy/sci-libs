# -*- coding: utf-8 -*-

import pylab as pl

# Definición de funciones auxiliares
def f1(x):
    return x**2

def f2(x):
    return x**3

def f3(x):
    return 1./x

def f4(x):
    return pl.sqrt(x)

X = pl.arange(1,100)
fig = pl.figure("Varios plots")
# Vamos a crear un grid de 2x2 con 4 subplots
sp1 = fig.add_subplot(221, title='$f(x) = x^2$')    # Ojo al titulo con expresión matemática
sp2 = fig.add_subplot(222, title='$f(x) = x^3$')
sp3 = fig.add_subplot(223, title= '$f(x) = \\frac{1}{x}$')
sp4 = fig.add_subplot(224, title = '$f(x) = \sqrt{x}$')

Y1 = f1(X)
Y2 = f2(X)
Y3 = f3(X)
Y4 = f4(X)

sp1.plot(X, Y1, color="red")
sp2.plot(X, Y2, color="blue")
sp3.plot(X, Y3, color="green")
sp4.plot(X, Y4, color="orange")

pl.show()
