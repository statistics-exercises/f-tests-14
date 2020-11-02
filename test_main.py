import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_testStatistic(self) : 
        mu, sig = np.zeros(4), np.zeros(4) 
        for i in range(4) : 
            mu[i] = sum( yields[i,:] ) / len( yields[i,: ] )
            sig[i] = ( 4 / 3 )*( sum( yields[i,:]*yields[i,:] ) / 4 - mu[i]*mu[i] )

        sse, mut, sst = 3*sum(sig), sum(mu) / 4, 0 
        for i in range(4) : sst = sst + 4*( mu[i] - mut )*( mu[i] - mut )
        F = ( sst / 3 )  / ( sse / 12 )
        self.assertTrue( np.abs( F - testStatistic( yields) )<1e-4, "Your code for calculating the test statistic is not working correctly" )
        
    def test_pvalue(self) : 
        F = testStatistic( yields )
        pval = 1 - scipy.stats.f.cdf( F, 3, 12 )
        self.assertTrue( np.abs( pval - pvalue( yields ) )<1e-7, "Your code for calculating the p-value is not working correctly" )
