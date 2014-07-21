#!/usr/bin/python

# Week 6 Problem 2
# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.

from __future__ import print_function
import sqlite3
import pandas as pd

def read_my_census(connection):
    # There's a bug in pandas 13.1 or below, where the index column (id)
    # has to be a string.
    # This is fixed in 14.0, where you can safely remove dtype conversion.
    my_census = pd.read_csv('ss12pil_sql.csv', header = None,
                            dtype = {'id': 'str'},
                            names = ['id', 'age', 'hours_worked', 'income'])
    # your code goes here
    return None

def read_more_census(connection):
    # There's a bug in pandas 13.1 or below, where the index column (id)
    # has to be a string.
    # This is fixed in 14.0, where you can safely remove dtype conversion.
    more_census = pd.read_csv('ss12pil_favorite_number.csv', header = None,
                              dtype = {'id': 'str'},
                              names = ['id', 'favorite_number'])
    # your code goes here
    return None

def join_census(connection):

    # your code goes here
    return None

def insert_me(connection):

    # your code goes here
    return None

def find_millionaires(connection):

    # your code goes here
    return dataframe

def main():
    # create a Connection object that represents the database
    conn = sqlite3.connect(':memory:')
    # read id, age, hourrs_worked, and income
    read_my_census(conn)
    # read id, and favorite_number
    read_more_census(conn)
    # join two tables
    join_census(conn)
    # insert a new row
    insert_me(conn)
    # save changes
    conn.commit()
    # issue a query and print the result
    df = find_millionaires(conn)
    print(df)
    # close connection
    conn.close()

if __name__ == '__main__':
    main()