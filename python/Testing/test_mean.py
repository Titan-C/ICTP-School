def mean(numlist):
   try :
       total = sum(numlist)
       length = len(numlist)
   except ValueError :
       print "The number list was not a list of numbers."
   except :
       print "There was a problem evaluating the number list."
   return total/length

class TestClass:
   def test_mean(self):
       assert(mean([0,0,0,0])==0)
       assert(mean([0,200])==100)
       assert(mean([0,-200]) == -100)
       assert(mean([0]) == 0)
   def test_floating_mean(self):
       assert(mean([1,2])==1.5)

