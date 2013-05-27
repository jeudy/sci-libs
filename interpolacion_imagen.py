from scipy.misc import imread, imsave
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

def func(x, y):
    #return np.sqrt(x**2 + y**2)+np.sin(x**2 + y**2)
    return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2

grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]
points = np.random.rand(1000, 2)
values = func(points[:,0], points[:,1])

grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
grid_z1 = griddata(points, values, (grid_x, grid_y), method='linear')
grid_z2 = griddata(points, values, (grid_x, grid_y), method='cubic')

plt.figure("Interpolacion para reconstruir imagenes")

plt.subplot(221)
plt.imshow(func(grid_x, grid_y), extent=(0,1,0,1))
plt.plot(points[:,0], points[:,1], 'k.', ms=1)
plt.title('Original')
plt.subplot(222)
plt.imshow(grid_z0, extent=(0,1,0,1))
plt.title('Nearest')
plt.subplot(223)
plt.imshow(grid_z1, extent=(0,1,0,1))
plt.title('Linear')
plt.subplot(224)
plt.imshow(grid_z2, extent=(0,1,0,1))
plt.title('Cubic')
plt.gcf().set_size_inches(6, 6)
plt.show()
