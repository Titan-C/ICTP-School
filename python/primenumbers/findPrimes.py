''' findPrimes.py
List whether the numbers passed in the command line are prime.
'''

from sys import argv
from math import sqrt

def isPrime(n):
	'''Returns True iff n is prime'''
	if n<=1:
		return False

	if n<=3:
		return True 

	if n%2 == 0: return False

	cntr = 3
	while cntr <=sqrt(n):
		if n%cntr == 0:
			return False
		cntr += 2
	return True

for i in range(1,len(argv)):
	primeTest = isPrime(int(argv[i]))
	if primeTest: print argv[i],"is prime"
	else: print argv[i],"is not prime"

