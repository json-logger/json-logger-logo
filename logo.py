#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plt.rc("font", family="Signika")
fig = plt.figure(figsize=(4, 4))
fig.text(0.5, 0.5, "{…}\no11y", ha="center", va="center", size=100)
fig.savefig("logo.svg")
plt.show()
