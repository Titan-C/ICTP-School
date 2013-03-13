import argparse
import random
import numpy as np
import time

parser = argparse.ArgumentParser(description='Benchmark Numpy arrays agains lists')

parser.add_argument('integers', metavar='N', type=int, nargs='+', help='Matrix lengh size')

args=parser.parse_args()
size=args.integers[0]

#Create List Matrices
A=[[int(random.random()*10) for i in range(size)] for j in range(size)]
#print A
B=[[int(random.random()*10) for i in range(size)] for j in range(size)]
#print B
C=[[0 for i in range(size)] for j in range(size)]
#print C

#Evaluate C=A*B
start=time.time()
for i in range(size):
  for j in range(size):
    for k in range(size):
      C[i][j]+=A[i][k]*B[k][j]
print time.time() -start
#print C

#Transform to NumPy
NA=np.array(A)
NB=np.array(B)

start=time.time()
NC=np.dot(A,B)
print time.time() -start
#print NC

