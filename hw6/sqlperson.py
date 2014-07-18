#!/usr/bin/python

# Week 6 Problem 3
# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.

from __future__ import print_function
import sqlite3
from person import OnePerson

def adapt_person(person):
    '''
    Takes a OnePerson object and returns a string representation of OnePerson.row.

    Example:
    >>> from person import OnePerson
    >>> p = OnePerson(['a', 'b', 'c'])
    >>> adapt_person(p)
    'a,b,c'
    '''
    # your code goes here
    return text

def convert_person(text):
    '''
    Takes a string and returns a OnePerson object constructed with the string.
    
    Example:
    >>> s = convert_person('a,b,c')
    >>> type(s)
    person.OnePerson
    >>> print(s.row)
    ['a', 'b', 'c']
    '''
    # your code goes here
    return person

def create_table(cursor):
    '''
    Executes an SQLite command that creates a table (name: "myCensus")
    with a column (name: "p", type: "person").
    Takes an sqlite3.Cursor object.
    Returns None if executed with no error.
    '''
    # your code goes here
    return None

def insert_person(cursor, person):
    '''
    Executes an SQLite command that inserts the values of the second argument
    ("person", OnePerson object) into a table (name: "myCensus")
    Takes an sqlite3.Cursor object and a OnePerson object.
    Returns None if executed with no error.
    '''
    # your code goes here
    return None

def print_head(cursor):
    '''
    Executes an SQLite query of all "person" columns from a table
    (name: "myCensus"), fetches one from cursor (which will be a OnePerson
    object), and use OnePerson.print_column() function (in a loop)
    to print out the first 10 columns.
    Takes an sqlite3.Cursor object.
    Returns None if executed with no error.
    '''
    # your code goes here
    return None
    
def main():
    # 2012 Illinois ACS PUMS file with NO pre-processing.
    filename = 'ss12pil.csv'

    # OnePerson class from week 3, store the 100th row in the object.
    p = OnePerson([])
    p.read_line(filename, 100)

    # tell sqlite3 library that we will be using our custom functions
    # adapt_person and convert_person as adapter and converter, respectively.
    sqlite3.register_adapter(OnePerson, adapt_person)
    sqlite3.register_converter('person', convert_person)

    # use memory for testing, you can change it to a filename and store it
    # note that we are using DECLARED TYPES.
    conn = sqlite3.connect(':memory:', detect_types = sqlite3.PARSE_DECLTYPES)
    cur = conn.cursor()

    # call our custom functions.
    create_table(cur)
    insert_person(cur, p)
    print_head(cur)

    # close connection.
    cur.close()
    conn.close()
    
if __name__ == '__main__':
    main()
