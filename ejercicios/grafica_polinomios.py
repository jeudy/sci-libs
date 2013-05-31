# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

f = np.poly1d([6, 9, 0, -2])

df = f.deriv()

x = np.linspace(-2, 2, 10)

y = f(x)

dy = df(x)

fig = plt.figure("Graficando polinomios")
sp1 = fig.add_subplot(121, title='$f(x) = 6x^3 + 9x^2 - 2$')
plt.xticks([-2, -1, 0, 1, 2])
sp2 = fig.add_subplot(122, title='$df(x)$')
sp1.plot(x, y, 'r+')
plt.xticks([-2, -1, 0, 1, 2])
sp2.plot(x, dy, 'b')

plt.show()