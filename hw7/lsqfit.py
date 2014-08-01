#!/usr/bin/python

# Week 7 problem 3. Least squares fit.

# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.
# Do not import other modules.
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def get_lsqfit(x, y):
    '''
    Takes two arrays and returns a tuple of two floats (slope and
    intercept of least squares fit).

    Examples:
    >>> import numpy as np
    >>> x = np.array([0.0, 1.0, 2.0])
    >>> y = np.array([0.0, 2.0, 4.0])
    >>> get_lsqfit(x, y)
    (2.0, 0.0)
    '''

    return slope, intercept

if __name__ == '__main__':

    # your code goes here