#!/usr/bin/python

# Week 7 problem 1. PMF, PDF, and CDF.

# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.
# Do not import other modules other than the ones listed here.

from __future__ import print_function, division
import matplotlib.pyplot as plt
import numpy as np
from stats2 import get_column

def get_histogram(sequence):
    '''
    Takes a list and returns a dictionary of the form {value: frequency}.

    Examples:
    >>> get_histogram(['a', 'a', 'b', 'b', 'b', 'c'])
    {'a': 2, 'b': 3, 'c': 1}
    >>> get_histogram([4, 5, 6, 6, 6])
    {4: 1, 5: 1, 6: 3}
    '''
    hist = {}

    # your code goes here
    
    return hist

def get_pmf(sequence):
    '''
    Takes a list and returns a dictionary of the form {value: probability}.

    Examples:
    >>> get_pmf(['a', 'a', 'b', 'b', 'b', 'c'])
    {'a': 0.3333333333333333, 'b': 0.5, 'c': 0.16666666666666666}
    >>> get_pmf([4, 5, 6, 6, 6])
    {4: 0.2, 5: 0.2, 6: 0.6}
    '''
    pmf = {}
    
    # your code goes here
    
    return pmf
    
def get_cdf(sequence):
    '''
    Takes a Numpy array and returns a tuple that represents
    the x and y axes of the empirical distribution function.

    Examples:
    >>> import numpy as np
    >>> x = np.array([4, 3, 1, 2, 5])
    >>> get_cdf(x)
    (array([1, 2, 3, 4, 5]), array([ 0.2,  0.4,  0.6,  0.8,  1. ]))
    '''

    # your code goes here
    
    return x, y

if __name__ == '__main__':

    filename = 'ss12pil.csv'

    # person's age is WKHP, the 72nd column in ss12pil.csv
    hours_worked = get_column(filename, 72)
    # remove people who didn't work (hours == 0) and some outliers
    hours_worked = [h for h in hours_worked if h > 0 and h < 80]
    # The PMF.
    hist = get_pmf(hours_worked)

    # peron's income is PINCP, the 103rd column in ss12pilcsv
    income = np.loadtxt(filename, delimiter = ',', skiprows = 1, usecols = (103, ),
                        converters = {103: lambda x: int(x or 0.0)})
    # remove some outliers (income below $1000)
    income = income[income > 1000]
    # The CDF
    cdf_x, cdf_y = get_cdf(income)
    # The CCDF
    ccdf_x, ccdf_y = cdf_x, 1.0 - cdf_y

    # you code goes here
