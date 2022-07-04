import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri


fig = plt.figure(figsize=plt.figaspect(0.5))

u = np.linspace(-1, 1, endpoint=True, num=25)
v = np.linspace(-1, 1, endpoint=True, num=25)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()

x = u
y = v
z = (u**2+v**2)**2 < .5

tri = mtri.Triangulation(u, v)

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)

plt.show()