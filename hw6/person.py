#!/usr/bin/python

# Week 3 problem 2

class OnePerson(object):
    '''
    Represents a row(one person) from the census file.

    Attributes:
      row (list of strings): stores a row representing one person as a list of strings.

    Methods:
      read_line(self, input_file, n)
      print_column(self, n)

    Examples:
    >>> p = OnePerson()
    >>> print(p.read_line('ss12pil.csv', 1)[:10]) 
    ['P', '38', '01', '01602', '17', '1010207', '00200', '50', '1', '']
    >>> p.print_column(0)
    Column 0 is: P
    >>> p.print_column(1)
    Column 1 is: 38
    '''
    def __init__(self, row = None):
        '''
        Initializer
        '''
        self.row = row
        
    def read_line(self, input_file, n):
        '''
        Takes the name of the file and the row number 'n',
        stores in the 'row' attribute the list representing the corresponding row,
        and returns that list.
        '''
        with open(input_file, 'r') as f:
            for i, line in enumerate(f):
                if i == n:
                    self.row =  line.strip().split(',')
                    break
        
    def print_column(self, n):
        '''
        Takes the column number 'n' and prints out the corresponding 'column' of
        the 'row' attribute.
        '''
        print('Column %i is: %s' % (n, self.row[n]))
    
if __name__ == '__main__':
    
    filename = 'ss12pil.csv'
    person = OnePerson()
    person.read_line(filename, 100)
    for i in xrange(10):
        person.print_column(i)