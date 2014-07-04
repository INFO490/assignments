#!/usr/bin/python

# Week 5 problem 1. Popular Baby Names.
# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.

from __future__ import print_function
from bs4 import BeautifulSoup
import requests
import pandas as pd

class BabyNames():
    '''
    A class BabyNames for scraping the Popular Baby Names page
    on Social Security website.

    Attributes:
      state(str): Two-letter abbreviation of state.
      year(str): Year from 1960 to 2013.
      fields(list): Headers of the table.

    Methods:
       get_page(self): fetches the HTML page and returns a unicode string.
       parse_page(self, page): takes a unicode string and returns a dictionary.

    '''
    def __init__(self, state = None, year = None):
        '''
        Constructor
        '''
        self.fields = [u'rank', u'male_name', u'number_of_males',
                       u'female_name', u'number_of_females']
        
        # your code goes here
            
    def get_page(self):
        '''
        Fetches the HTML page using requests.
        Returns a string (unicode).
        '''
        url = "http://www.ssa.gov/cgi-bin/namesbystate.cgi"
        query = {'year': self.year, 'state': self.state}
        
        r = # your code goes here
        
        return r.text

    def parse_page(self, page):
        '''
        Use Beautiful Soup to parse the HTML page fetched with get_page().
        Takes string (unicode) and returns a dictionary.
        The keys of the dictionary are the column headers (self.fields).
        The values of the dictionary are the a list of values corresponding
        to the column.
        
        Parameters:
          page (unicode): A unicode string returned from get_page() function.
                          See requests.post().text.
        Examples:
        >>> b = BabyNames(state = 'IL', year = '2013')
        >>> p = b.get_page()
        >>> d = b.parse_page(p)
        >>> print(d.keys())
        [u'female_name', u'number_of_females', u'male_name', u'rank', u'number_of_males']
        >>> print(len(d[u'number_of_females']))
        101
        >>> print(d[u'number_of_females'][:5])
        [u'881', u'851', u'786', u'671', u'558']
        >>> print(d[u'female_name'[:5]])
        [u'Olivia', u'Sophia', u'Emma', u'Isabella', u'Emily']
        '''

        # your code goes here
        
        return data

if __name__ == '__main__':

    # create a class BabyNames for 2013 Illinois
    b = BabyNames(state = 'IL', year = '2013')
    # fetch the HTML page
    p = b.get_page()
    # parse the HTML page, data is a dictionary
    d = b.parse_page(p)
    # print top 5 names
    print('Top 5 baby names')
    print('Females: ' + ', '.join('{}({})'.format(
          d[u'female_name'][i], d[u'number_of_females'][i]) for i in xrange(5)))
    print('Males: ' + ', '.join('{}({})'.format(
          d[u'male_name'][i], d[u'number_of_males'][i]) for i in xrange(5)))
