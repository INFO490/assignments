#!/usr/bin/python

from __future__ import print_function
import sqlite3
import pandas as pd

def read_my_census(connection):
    my_census = pd.read_csv('ss12pil_sql.csv', header = None,
                              names = ['id', 'age', 'hours_worked', 'income'])
    # your code goes here
    return None

def read_more_census(connection):
    
    more_census = pd.read_csv('ss12pil_favorite_number.csv', header = None,
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