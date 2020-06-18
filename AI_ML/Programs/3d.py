import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
def f(x,y):
    return np.sin(np.sqrt(x**2+y**2))

x = np.linspace(-6,6,30)
y = np.linspace(-6,6,30)

X,Y = np.meshgrid(x,y)
z = f(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X,Y,z,color='g')
ax.plot_surface(X,Y,z,cmap='coolwarm')
ax.set_title('surface')
plt.show()