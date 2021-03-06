import rainfall as rf
import random as rnd
from numpy.testing import assert_almost_equal

def test_rnd_99():
    '''
    Generate a list of random integers:

    - of length [0:50] 
    - in the range [0:99)

    In this notation the square bracket indicates inclusive, the parentheses exlusive i.e.

    Find the mean then add a terminating 99 and further 'fluff' values, 
    Then disperse negative values in the resulting list.

    Finally test rfmean against the expected value.
    '''

    rnd.seed()

    # Conduction 50 tests of:

    for itest in range(50):

        # Generate number of values
        nvalues = rnd.randrange(51)

        # Generate list of non-negative random numbers less thann 99
        values = []
        for ivalue in range(nvalues):
            values.append( rnd.randrange(99) )

        # Calculate expected mean
        expect = sum(values) / nvalues

        # Add terminating 99
        values.append(99)

        # Add some fluff after 99
        fluff = []
        for ivalue in range(50):
            fluff.append( rnd.randrange(100) )
        values.extend( fluff )

        # Disperse some (fewer than 11) negative numbers [-10:0)
        for x in range( rnd.randrange(1,11) ):
            insert_value = rnd.randrange(-10,0)
            insert_pos = rnd.randrange( len(values) )
            values.insert( insert_pos, insert_value )

        assert_almost_equal( rf.rfmean(values), expect)
