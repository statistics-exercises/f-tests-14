import numpy as np
import scipy.stats

def testStatistic( data ) : 
  # Your code to calculate the test statistic from the input data
  # goes here
  

def pvalue( data ) : 
  F = testStatistic( data )
  # Your code to compute the p-value from the test statistic goes here
  
  
yields = np.zeros([4,4])
yields[0,:] = [38.3,38.5,38.7,41.2]
yields[1,:] = [38.8,43.4,38.9,39.1]
yields[2,:] = [40.3,42.6,41.1,40.6]
yields[3,:] = [62.7,61.0,54.8,51.7]
print("Null hypothesis: The expectations of the four distributions that have been sampled are all identical")
print("Alternative hypothesis: The expectations of the four distributions are not all identical")
print("The p-value for this hypothesis test is", pvalue( yields ) )
