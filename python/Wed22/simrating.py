# -*- coding: utf-8 -*-
'''Calculates similarity in order to generate Recommendations for papers'''

import inputdata, numpy
from scipy.stats import  pearsonr as cor
data = inputdata.raw_scores
sreaders=set()
spapers=set()
class infbase(object):
  '''Database'''
  def __init__(self):

    for reader,read in data.items():
      sreaders.add(reader)
      for paper in read.iterkeys():
        spapers.add(paper)

    self._readers = list(sreaders)
    self._papers = list(spapers)
    self._rankings = numpy.zeros((len(self._readers),len(self._papers)))

    for reader,read in data.items():
      i=self._readers.index(reader)
      for paper,rank in read.items():
        j=self._papers.index(paper)
        self._rankings[i][j] = rank

  def readersvec(self,a,b):
    r1=a[numpy.logical_and(a,b)]
    r2=b[numpy.logical_and(a,b)]
    return r1, r2

  def norm_eval(self,a,b):
    return numpy.linalg.norm(a-b)

  def pearson_eval(self,a,b):
    r,e = cor(a,b)
    return r

  def similarity_eval(self,base,comp):
    r1, r2 = self.readersvec(base,comp)
    n = self.norm_eval(r1,r2)
    r = self.pearson_eval(r1,r2)
    return numpy.abs(r/n)
  
  def listmostsimilar(self,id,suject):
    if suject == 'paper':
      matrix = self._rankings.T
    else :
      matrix = self._rankings
    
    reco=[0]*len(matrix)
    base = matrix[id]
    for j in range(len(matrix)):
      if j == id :
	continue
      reco[j] = self.similarity_eval(base,matrix[j])
    return reco

  def mostsimilar(self,ranked,suject):
    top = sorted(ranked,reverse=True)
    for i in range(5):
      if suject == 'paper':
	print i+1, '.- ', self._papers[ranked.index(top[i])]
      else:
	print i+1, '.- ', self._readers[ranked.index(top[i])]
      
      
      


trabajo = infbase()
#print trabajo._readers
#print trabajo._papers
print trabajo._rankings
#import pdb; pdb.set_trace()
for id in range(7):
  print 'Most similar researchers to ',trabajo._readers[id], 'are:'
  ranked = trabajo.listmostsimilar(id,'researchers')
  trabajo.mostsimilar(ranked,'researchers')
for id in range(6):
  print 'Most similar papers to ',trabajo._papers[id], 'are:'
  ranked = trabajo.listmostsimilar(id,'paper')
  trabajo.mostsimilar(ranked,'paper')