#!/usr/bin/python

# Week 2 Problem 3. Simple statistics.

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

    # min() and max() are in the standard library
    # you could also write
    # minimum = sorted(input_list)[0]
    # maximum = sorted(input_list)[-1]
    minimum = min(input_list)
    maximum = max(input_list)

    # use the sum() function from the standard library to calculate mean
    # this is equivalent to
    # total = length = 0
    # for i in input_list: total += i
    # for i in input_list: length += 1
    # mean = total / length
    mean = sum(input_list) / len(input_list)

    # calculate the median
    # if the number of elements is even, we take the average of 2 middle numbers
    # if the number of elements is odd, median is the middle element
    # note that we used the Python 3 integer division // to get integer
    if len(input_list) % 2:
        median = input_list[(len(input_list) - 1) // 2 ]
    else:
        median = 0.5 * (input_list[(len(input_list) - 1) // 2] \
                        + input_list[len(input_list) // 2])

    # return a tuple of min, max, mean, median
    return minimum, maximum, mean, median
    
if __name__ == '__main__':

    # we will test our function with a list of integers from 0 to 50
    my_list = range(0, 51)

    # get_stats returns a tuple of min, max, mean, median of my_list
    # print out min, max, mean, median on each line
    print("Minimum: %i\nMaximum: %i\nMean: %.1f\nMedian: %.1f" % get_stats(my_list))