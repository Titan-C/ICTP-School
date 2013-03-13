#Problems from Projecteuler.net

#Problem #1
def multiples3_5(top):
  mults=[]
  for x in range(top):
    if x % 3 ==0 or x % 5==0:
      mults.append(x)
  s=0
  for x in mults:
    s=s+x
  print mults
  print s

multiples3_5(1000)

#Problem #24
import itertools
[x for x in itertools.permutations(range(10))][999999]
#
#if __name__ == "__main__":
