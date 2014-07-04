#!/usr/bin/python

# Week 5 problem 2. Simple Statistics Using Pandas

# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.

from __future__ import print_function
import numpy as np
import pandas as pd

def read_census(filename):
    '''
    Takes a filename(str) and returns a pandas.DataFrame object.

    Examples:
    >>> read_census('ss12pil.csv').shape
    (127208, 286)
    >>> read_census('ss12pil.csv')['AGEP'].head()
    0    50
    1    45
    2    26
    3    87
    4    41
    Name: AGEP, dtype: int64
    '''

    # your code goes here
    
    return dataframe
    
def get_stats(dataframe, column):
    '''
    The first argument is a pandas.DataFrame object and
    the second argument is the column header(str).
    Returns a tuple of minimum, maximum, mean, and median
    of the specified column in the Pandas table.

    Examples:
    >>> df = read_census('ss12pil.csv')
    >>> get_stats(df, 'WKHP')
    (0.0, 99.0, 19.413079366077604, 10.0)
    >>> get_stats(df, 'AGEP')
    (0, 94, 40.174014212942581, 41.0)
    '''
    
    # your code goes here.
    
    return minimum, maximum, mean, median

if __name__ == '__main__':

    infile = 'ss12pil.csv'
    
    fields = [('PWGTP', "The integer weight of each person"),
          ('AGEP', "The person's age"),
          ('MARHT', "The number of times married"),
          ('WKHP', "The usual hours worked per week past 12 months")]

    df = read_census(infile)
    
    for col, title in fields:
        print(title)
        print("Minimum: %i\nMaximum: %i\nMean: %.1f\nMedian: %.1f\n"
              % get_stats(df, col))