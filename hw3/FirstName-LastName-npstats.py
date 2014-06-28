#!/usr/bin/python

# Week 3 Assignment Problem 3
# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.

# use Python 3 print() function
from __future__ import print_function, division
import numpy as np

def get_columns(filename):
    '''
    Takes a file and returns a 2-D numpy array of columns 6, 7, 39, and 72.

    Parameters:
      filename(str): the name of the CSV file
    Examples:
    >>> get_columns('ss12pil.csv').shape
    (4, 127208)
    >>> get_columns('ss12pil.csv')[0, :10]
    array([ 200.,   70.,  212.,   15.,   71.,   80.,   95.,  131.,  147.,  149.])
    '''
    result = np.loadtxt( # your code goes here )
    
    return result
    
def print_stats(input_array, title = None):
    '''
    Computes minimum, maximum, mean, and median using numpy functions,
      and prints them out in a nice format.

    Parameters:
      input_array(numpy.ndarray): a numpy array representing a column
      title(str): Optional. If given, title is printed out before the stats.

    Examples:
    >>> import numpy as np
    >>> print_stats(np.array([1, 2, 3, 4, 5]))
    Minimum: 1
    Maximum: 5
    Mean: 3.0
    Median: 3.0
    >>> print_stats(np.array([1, 2, 3, 4, 5, 6]), 'Stats!')
    Stats!
    Minimum: 1
    Maximum: 6
    Mean: 3.5
    Median: 3.5
    '''

    # your code goes here
    
    return None
    
if __name__ == '__main__':

    # your code goes here