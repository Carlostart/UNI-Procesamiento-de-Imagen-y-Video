import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

h,w = signal.freqz([-1,2,-1])
print(h)
print(w)

plt.scatter(range(h.__len__()),w)
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.seismic)
plt.show()