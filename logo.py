#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plt.rc("font", family="Signika")

x = np.linspace(0, 1, 1023)
y = x[::-1]
x_grid, y_grid = np.meshgrid(x, y)
z_grid = np.sqrt(x_grid**2 + y_grid**2)

fig, ax = plt.subplots()
ax.axis("off")
ax.imshow(z_grid, cmap="Greys", vmin=0, vmax=2)
ax.text(x_grid.shape[0] / 2, x_grid.shape[1] / 2, "{…}\no11y", color="#7F7F7F", ha="center", va="center", size=120)
fig.savefig("logo.jpg", pad_inches=0)
plt.show()
