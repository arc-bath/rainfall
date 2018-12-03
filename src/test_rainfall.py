import rainfall as rf
from numpy.testing import assert_almost_equal

# A series of test for the rainfall problem

def test_rf_simple_1():
    '''
    A simple test which has no negative and no '99's
    '''
    test_list = [ 1 ]

    expect = test_list[0]
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )

def test_rf_simple_2():
    '''
    A simple test which has no negative and no '99's
    '''
    test_list = [ 2.35 ]

    expect = test_list[0]
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )

def test_rf_simple_3():
    '''
    A simple test which has no negative and no '99's
    '''
    test_list = [ 1, 2, 3, 4, 5 ]

    expect = test_list[2]
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )

def test_rf_negative_1():
    '''
    A test with negatives
    '''
    test_list = [ 1, 2, 3, 4, 5, -1]

    expect = test_list[2]
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )

def test_rf_negative_2():
    '''
    A test with negatives
    '''
    test_list = [ 1, 2, 3, -1, 4, 5]

    expect = test_list[2]
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )

def test_rf_negative_3():
    '''
    A test with negatives
    '''
    test_list = [ -1, 2, 3, 1, 4, 5]

    expect = test_list[2]
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )

def test_rf_negative_4():
    '''
    A test with negatives
    '''
    test_list = [ 2, 3, 4, -10, 5, 6, -10, 4, 4, 4]

    expect = test_list[2]
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )

def test_rf_99_1():
    '''
    A test with 99s
    '''
    test_list = [ 2, 3, 4, 99]

    expect = test_list[1]
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )

def test_rf_99_2():
    '''
    A test with 99s
    '''
    test_list = [ 2, 3, 4, 99, 5, 6, 99, 4, 4, 4]

    expect = test_list[1]
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )

def test_rf_both():
    '''
    A test with negatives and 99s
    '''
    test_list = [ 2, 3, 4, 99, 5, -1, 6, 99, 4, 4, 4]

    expect = test_list[1]
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )
    
def test_rf_empty():
    '''
    A test with empty list
    '''
    test_list = []

    expect = "Empty list"
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )
    
def test_rf_99_start():
    '''
    A test where first value is 99
    '''
    test_list = [99]

    expect = "First value 99"
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )
    
def test_rf_negative_99_start_1():
    '''
    A test with no valid data points
    '''
    test_list = [-1, 99]

    expect = "No valid data points"
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )
    
def test_rf_negative_99_start_2():
    '''
    A test with no valid data points
    '''
    test_list = [-1, -10, 99]

    expect = "No valid data points"
    observ = rf.rfmean( test_list )

    assert_almost_equal( observ, expect )
