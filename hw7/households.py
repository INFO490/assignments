#!/usr/bin/python

# Week 7 problem 2. The locomotive problem.

# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.
# Do not import other modules.
from __future__ import print_function
import numpy as np

def get_hypotheses(start = 1, end = 12880001):
    '''
    Takes two integers (the first serial number 1 and the final serial number N + 1).
    Returns a Numpy array of integers [1, 2, ..., N].

    Examples:
    >>> get_hypotheses(1, 5)
    array([1, 2, 3, 4])
    '''

    # your code goes here
    
    return result

def get_uniform_prior(hypotheses):
    '''
    Takes an array (an array of hypotheses) and
    returns a Numpy array of floats (an array of uniform prior).

    Examples:
    >>> import numpy as np
    >>> x = np.array([1, 2, 3, 4, 5])
    >>> get_uniform_prior(x)
    array([ 0.2,  0.2,  0.2,  0.2,  0.2])
    '''
    
    # your code goes here
    
    return result

def get_likelihood(data, hypotheses):
    '''
    Takes an integer (data) and an array (hypotheses)
    Returns a Numpy array of floats (likelihood).

    Examples:
    >>> import numpy as np
    >>> x = np.array([1, 2, 3, 4, 5])
    >>> get_likelihood(1, x)
    array([ 1.        ,  0.5       ,  0.33333333,  0.25      ,  0.2       ])
    >>> get_likelihood(2, x)
    array([ 0.        ,  0.5       ,  0.33333333,  0.25      ,  0.2       ])
    >>> get_likelihood(3, x)
    array([ 0.        ,  0.        ,  0.33333333,  0.25      ,  0.2       ])
    >>> get_likelihood(6, x)
    array([ 0.,  0.,  0.,  0.,  0.])
    '''

    # your code goes here
    
    return result

def get_posterior(data, hypotheses):
    '''
    Takes an integer (data) and an array (hypotheses).
    Returns a Numpy array of floats (posterior).

    Examples:
    >>> import numpy as np
    >>> x = np.array([1, 2, 3, 4, 5])
    >>> get_posterior(1, x)
    array([ 0.4379562 ,  0.2189781 ,  0.1459854 ,  0.10948905,  0.08759124])
    >>> get_posterior(2, x)
    array([ 0.        ,  0.38961039,  0.25974026,  0.19480519,  0.15584416])
    >>> get_posterior(3, x)
    array([ 0.        ,  0.        ,  0.42553191,  0.31914894,  0.25531915])
    >>> get_posterior(5, x)
    array([ 0.,  0.,  0.,  0.,  1.])
    '''

    # your code goes here
    
    return result

def get_estimate(posterior, hypotheses):
    '''
    Takes a two arrays (posterior and hypotheses).
    Returns a float (estimate).

    Examples:
    >>> import numpy as np
    >>> x = np.array([0.25, 0.25, 0.5])
    >>> y = np.array([1, 2, 3])
    >>> get_estimate(x, y)
    2.25
    '''

    # your code goes here
    
    return result

if __name__ == '__main__':
    # the last household in ss12pil.csv has serial number 1493780
    serialno = 1493780
    
    hypo = get_hypotheses()
    like = get_likelihood(serialno, hypo)
    post = get_posterior(serialno, hypo)
    estimate = get_estimate(post, hypo)
    
    print('Estimated number of households: %i' % (estimate, ))