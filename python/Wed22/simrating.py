# -*- coding: utf-8 -*-
'''Calculates similarity in order to generate Recommendations for papers'''

import inputdata, numpy
from scipy.stats import  pearsonr as cor
#import pdb; pdb.set_trace()
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

  def readersvec(a,b):
    r1=a[numpy.logical_and(a,b)]
    r2=b[numpy.logical_and(a,b)]
    return r1,r2

  def simcheck(a,b):
    return numpy.linalg.norm(r1-r2)

  def pearsontest(a,b)
    return cor(a,b)


trabajo = infbase()
print trabajo._readers
print trabajo._papers
print trabajo._rankings