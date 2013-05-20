# Ejemplo basado en del libro PythonScientific, capitulo 4

import pylab as pl
import numpy as np

# Create a figure of size 8x6 points, 80 dots per inch
pl.figure("Pruebas de plots", figsize=(8, 6), dpi=80)

# Create a new subplot from a grid of 1x1
pl.subplot(1, 1, 1)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
# Plot cosine with a red continuous line of width 1 (pixels)
pl.plot(X, C, color="red", linewidth=1.0, linestyle="-")
# Plot sine with a green continuous line of width 1 (pixels)
pl.plot(X, S, color="green", linewidth=1.0, linestyle="-")
# Set x limits
pl.xlim(-4.0, 4.0)
# Set x ticks
pl.xticks(np.linspace(-4, 4, 9, endpoint=True))
# Set y limits
pl.ylim(-1.0, 1.0)
# Set y ticks
pl.yticks(np.linspace(-1, 1, 5, endpoint=True))
# Save figure using 72 dots per inch
# Show result on screen
pl.title('Funciones Seno y Coseno de -pi a pi')
pl.show()
