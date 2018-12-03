

def rfmean(sample):
    '''
    Prototype function to return the 'rainfall' mean  of a sample

    Usage: rfmean( <list_of_numbers> ) 

    should return the mean subject with caveats that:
        negative numbers are ignored
        if `99` is read the calculation should stop and return the mean of valud preceding numbers

    test_rainfall.py contains tests which require:
   
    1. Modifying the function to solve the rainfall problem and
    2. Introduce checks to deal with empty lists/data sets
    '''

    sum = 0
    count = 0

    for value in sample:
        sum+=value
        count=count+1

    return sum/count
