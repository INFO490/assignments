#!/usr/bin/python

# Week 2 Problem 3. Simple statistics.
# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.

# Use Python 3 print() function, Python 3 integer division
from __future__ import print_function, division

def get_stats(input_list):
    '''
    Accepts a list of integers, and returns a tuple of four numbers:
    minimum(int), maximum(int), mean(float), and median(float)

    >>> get_stats([0, 1, 2, 3, 4])
    (0, 4, 2.0, 2.0)
    >>> get_stats([0, 1, 2, 3, 4, 5])
    (0, 5, 2.5, 2.5)
    >>> get_stats([0, 1, 2, 5])
    (0, 5, 2.0, 1.5)
    >>> get_stats([0, 1, 2, 4, 5])
    (0, 5, 2.4, 2.0)
    ''' 
    
    # your codes goes here.

    return minimum, maximum, mean, median
    
if __name__ == '__main__':

    my_list = # your code goes here. Use range() to generate a list.
    
    print("Minimum: %i\nMaximum: %i\nMean: %.1f\nMedian: %.1f" % get_stats(my_list))