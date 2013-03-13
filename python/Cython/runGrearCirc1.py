import timeit  

lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
num = 500000

t = timeit.Timer("p1.great_circle(%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2), 
                       "import greatCirc1 as p1")
print "Pure python function", t.timeit(num), "sec"

t = timeit.Timer("c1.great_circle(%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2), 
                       "import greatCirc2 as c1")
print "Cython function with python math", t.timeit(num), "sec"
