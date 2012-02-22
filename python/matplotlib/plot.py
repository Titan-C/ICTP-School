from matplotlib import pyplot as plt
x = range(0,10)
y = [val**2 for val in x]
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ax1.plot(x,x)
ax1.plot(x,y)
ax2.plot(x,y)
ax3.plot(x,y)
ax4.plot(x,x)
ax1.set_title('Noo')
fig.suptitle('The figure')
plt.show()
import numpy as np

r = np.linspace(0.1,2,200)
t = np.linspace(np.pi/4,7*np.pi/4,200)
r,t = np.meshgrid(r,t)
x = r*np.cos(t)
y = r*np.sin(t)
z = (x+0.6)**2 + (y-1.)**2

ax = plt.subplot(111)

ax.pcolor(x,y,z[1:,1:])
# ax.colorbar()

con = ax.contour(x,y,z)
ax.clabel(con)

plt.show()
