from scipy.special import * 
from pylab import *

x = arange(0.0, 10.1, 0.1)

for n in range(4):
	j = jn(n, x)
	plot(x, j, 'k-') 
	text(x[10*(n+1)+1], j[10*(n+1)], r'$J_%r$'%n)

for n in range(3): 
	y = yn(n, x) 
	plot(x, y, 'k--') 
	text(x[10*(n)+6], y[10*(n)+5], r'$Y_%r$'%n)

axis([0, 10, -2, 1.25]) 
xlabel(r'$x$') 
ylabel("Bessel Functions")

show()
