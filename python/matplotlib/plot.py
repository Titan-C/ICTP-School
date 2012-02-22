from matplotlib import pyplot as plt
x = range(0,10)
y = [val**2 for val in x]
ax = plt.subplot(111)
ax.plot(x,y)
plt.show()
