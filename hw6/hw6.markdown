## Week 6 assignment

For up-to-date version of this document, use Git or see [week 6 assignment](https://github.com/INFO490/assignments/blob/master/hw6/hw6.markdown) on GitHub.

### Installing SQLite

To install _SQLite 3_ in Ubuntu, use the following command:

    $ sudo apt-get install sqlite3

### Problem 1. SQLite from Command Line

Grab the template: [census.sql](https://github.com/INFO490/assignments/blob/master/hw6/census.sql)

#### Overview

In this problem, we will use the _SQLite_ command line tool to perform some simple database tasks. There are two ways to use the _SQLite_ command line tool. You can either simply do

    $ sqlite3 mydatabase.db
    SQLite version 3.8.5 2014-06-04 14:06:34
    Enter ".help" for usage hints.
    sqlite> 

which brings up an interactive prompt, where you can enter SQL commands line by line; or you can write an SQL script in text file format (e.g. `census.sql`), and run it from the command line with 

    $ sqlite3 mydatabase.db < census.sql

You might find it easier to practice and debug using the first option, but for submission, you will have to write an SQL script and make sure that the second method works.

Read the directions below at least once __before__ you start writing code to understand where you are headed. If you don't understand something in the directcions, review the lessons, google what you don't understand, or just ask us.

There are five major tasks in this problem:

1. CREATE a table named *myCensus*, import *ss12pil_sql.csv*,
2. CREATE another table *moreCensus*, import *ss12pil_favorite_number.csv*,
3. JOIN *myCensus* and *moreCensus* by matching the PRIMARY KEY,
4. INSERT a new row in the table,
5. SELECT query.

#### Creating a new table

Your first task is to create a table and import the Illinois census data. Although _SQLite_ can import CSV files, some pre-processing is still necessary. We will use the columns *SERIALNO*, *SPORDER*, *AGEP*, *WKHP*, and *PINCP* in _ss12pil.csv_. Columns AGEP*, *WKHP*, and *PINCP* should be familar to you. *SERIALNO* is a unique serial number that identifies each household, and *SPORDER* is an identifier that distinguishes each person in the household. Thus, when we combine these two numbers, we have a unique identifier for every person. We will use this combination as the PRIMARY KEY in SQLite. Let's extract these columns and make a CSV file that can easily be imported by SQLite:

    $ sed 1d ss12pil.csv | awk -F, '{if($73 == ""){$73 = 0}; if($104 == ""){$104 = 0}; print $2$3 "," $8 "," $73 "," $104}' > ss12pil_sql.csv

Put this file *ss12pil_sql.csv* in the same directory as the template file. Now, open up the template, and in your SQL script the first thing you should do is

- CREATE a new table named _myCensus_ with four columns, *id* (PRIMARY KEY), *age*, *hours_worked*, and *income*.

All columns are integers, and the first column (*id*) should be PRIMARY KEY.

Next, since *ss12pil_sql.csv* is still a CSV file, we have to tell *SQLite* that the file is separated by commas as follows.

    sqlite> .separator ,
    sqlite> .import ss12pil_sql.csv myCensus

Note that you have to create a new table __before__ importing a CSV file. Above commands import the CSV file into a table named *myCensus*.

#### Creating another table

Grab the CSV file: [ss12pil\_favorite\_number.csv](https://github.com/INFO490/assignments/blob/master/hw6/ss12pil_favorite_number.csv)

You have just finished creating a table from the , but someone comes along and hands you another CSV file, *ss12pil_favorite_number.csv*. This file was created by going around and asking each person in the *ss12pil.csv* file what his or her favorite single-digit number is. Note it is not in the same order as the original census file, i.e.

    $ head -3 ss12pil_sql.csv 
    3801,50,0,000121000
    3802,45,40,000027000
    3803,26,40,000020000
    $ head -3 ss12pil_favorite_number.csv 
    50995101,8
    131478101,2
    81532401,2

- CREATE a new table named _moreCensus_ with two columns, *id* (PRIMARY KEY) and *favorite_number*. Import *ss12pil_favorite_number.csv*.

#### Joining tables

Now we want to join this newly created table *moreCensus* with the original table *myCensus*.

- JOIN (or INNER JOIN) _myCensus_ and _moreCensus_ by matching PRIMARY KEY. Combine them into a new table _myMoreCensus_.

#### Inserting

At this point, you decide for some reason that you may as well enter your own information into the table.

- INSERT a new row into *myMoreCensus*. Assume that in 2012
 - your PRIMARY KEY is 49001,
 - you were 21 years old,
 - worked 40 hours a week,
 - made one million dollars, and
 - your favorite number is 1.

#### Query

Finally, use

- a SELECT statement to find every person in 2012
 - who was 18 years of age or older, and
 - who worked 40 hours or more per week, and
 - whose annual income exceeded $500,000, and
 - whose favorite digit is 1.

The answer should be

    21504101,58,55,607000,1
    66592402,62,50,540000,1
    93004702,71,72,607000,1
    121640701,48,40,607000,1
    133309001,33,45,560000,1
    148470501,51,70,733000,1
    49001,21,40,1000000,1

#### Submission Instructions

Make sure that your SQL script runs without a problem when you do

    $ sqlite3 mydatabase.db < census.sql

Rename your file to `<firstname>-<lastname>-census.sql` and upload it to Moodle.

### Problem 2. SQLite in Python

- Grab the template: [sqlcensus.py](https://github.com/INFO490/assignments/blob/master/hw6/sqlcensus.py)

#### Overview

In this problem, you will repeat the same task in Problem 1 using the *sqlite3* library in Python. 

Before you start, browse the template file and try to see the big picture. Read the directions below at least once before you start writing anything. This problem should not be too hard if you understood Problem 1 because it's a straightforward Python implementation of Problem 1.

You have to write 5 functions:

- read\_my\_census()
- read\_more\_census()
- join\_census()
- insert\_me()
- find\_millionaires()

These functions are divided up so that each function can be written in one or two lines at most. As the function names suggest, each function corresponds to one operation or one SQL statement.

Note that the functions *read_my_census()*, *read_more_census()*, *join_census()*, and *insert_me()* all take an *sqlite3.Connection* object as an argument (and return *None*). The fifth function *find_millionaires()* takes an *sqlite3.Connection* object as an argument and returns a *pandas.DataFrame* object.

#### Function: main()

The _main()_ function will create a *sqlite3.Connection* object, call each of above functions in turn, and print out the result. The final result should be

              id  age  hours_worked   income  favorite_number
    0   21504101   58            55   607000                1
    1   66592402   62            50   540000                1
    2   93004702   71            72   607000                1
    3  121640701   48            40   607000                1
    4  133309001   33            45   560000                1
    5  148470501   51            70   733000                1
    6      49001   21            40  1000000                1

#### Function: read_my_census()

- Use *pandas.read_csv()* and *pandas.to_sql()* functions to read the *ss12pil_sql.csv* file and convert it to a table named *myCensus*.

#### Function: read_my_census()

- Use *pandas.read_csv()* and *pandas.to_sql()* functions to read the *ss12pil_favorite_number.csv* file and convert it to a table named *moreCensus*.

#### Function: join_census()

The *join_census()* function joins _myCensus_ and _moreCensus_ tables into a new table named *myMoreCensus*. It is probably easiest to

- Use the same command from Problem 1 as an argument to the *execute()* method.

#### Function: insert_me()

This function inserts a new row into the *myMoreCensus* table. You should use the same values you used in Problem 1.

- Use the same command from Problem 1 as an argument to the *execute()* method.

#### Function: find_millionaires()

The *find_millionaires()* function takes an *sqlite3.Connection* object as an argument and returns a *pandas.DataFrame* object.

- Use *pandas.read_sql()* method to issue the same query as in Problem 1 and return the result as a *pandas.DataFrame* object.

#### Submission Instructions

Rename your file to `<firstname>-<lastname>-sqlcensus.py` and upload it to Moodle.

### Problem 3. Python Objects in SQLite

- Grab the template: [sqlperson.py](https://github.com/INFO490/assignments/blob/master/hw6/sqlperson.py)

#### Overview

- Read [SQLite and Python types](https://docs.python.org/3.4/library/sqlite3.html#sqlite-and-python-types).

In this problem, you will use a class object to interact with *SQLite*. Make sure you read the section [SQLite and Python types](https://docs.python.org/3.4/library/sqlite3.html#sqlite-and-python-types) in the official Python documentation. This problem and the template file follow one of the sample codes very closely, so read the above link very carefully. Read the directions at least once __before__ you start writing any code. Browse the template file at least once to get the big picture. If you don't understand something in the code or the directcions, review the lessons, google what you don't understand, or just ask us.

You have to write 5 functions:

- adapt_person()
- convert_person()
- create_table()
- insert_person()
- print_head()

These functions are divided up so that each function can be written in one or two lines at most (except maybe the *print_head()* function which can be written in 3 or 4 lines).

Recall that in week 3 assignment you wrote a class named _OnePerson_ that represents a row in the Illinois census file. All you have to do in this problem is modify the sample code (which uses *Point* object) in the above link to use our _OnePerson_ object. Thus, you will need to import _person.py_ module you wrote. If you want to use your own code, you will have to make sure that it is possible to construct the class by passing a list, e.g.

    person = OnePerson(['a', 'b', 'c'])

that is, your initializer should be something like

    def __init__(self, row = None):
		self.row = row

If you are not sure your code will behave correctly, you can download and use my version of [person.py](https://github.com/INFO490/assignments/blob/master/hw6/person.py) from GitHub.

At the end, your code should produce exactly the same output as the code from week 3, i.e. read the 100th line of the census file and print out the first 10 columns.

    Column 0 is: P
    Column 1 is: 1142
    Column 2 is: 01
    Column 3 is: 03408
    Column 4 is: 17
    Column 5 is: 1010207
    Column 6 is: 00203
    Column 7 is: 43
    Column 8 is: 5
    Column 9 is: 

Only this time, you will do this by interacting with an SQL database. As the official Python documentation explains, in order to move back and forth between Python and SQLite, we need an adaptor that sends the _OnePerson_ class to *SQLite* by representing the object as a string, and a converter that accepts the string representation and reconstructs a _OnePerson_ object.

#### Function: main()

Read the *main()* function first to understand the flow of the code. This function is already written and provided for you, so you don't have to change anything here.

#### Function: adapt_person()

- Write a function named *adapt_person()* that accepts a _OnePerson_ object as an argument and returns a string representation of _OnePerson.row_ (each item in the list separated by commans).

This function will be used in *sqlite3.register_adapter()* method to make *SQLite* aware how to translate our *OnePerson* object to an SQL data type *person*.

#### Function: convert_person()

- Write a function named *convert_person()* that accepts a string and returns a *OnePerson* object constructed from the string.

This function will be used in *sqlite3.register_converter()* method to make *SQLite* aware how to translate an SQL data type *person* back to our *OnePerson* object.

#### Function: create_table()

- Write a function named *create_table()* that accepts an *sqlite3.Cursor* object and creates an SQL table named *myCensus*, which stores an instance of *OnePerson* object.

#### Function: insert_person()

- Write a function named *insert_person()* that accepts an *sqlite3.Cursor* object as the first argument and a *OnePerson* object as the second argument. It then inserts the values of *OnePerson* object into the *myCensus* table created by the *create_table()* function.

#### Function: print_head()

- Write a function named *print_head()* that accepts an *sqlite3.Cursor* object. It should first execute a SELECT statement that retrieves the instance of *OnePerson* object stored in the *myCensus* table. It should then call the cursor's *fechone()* or *fetchall()* to retrieve the *OnePerson* object. Use the *OnePerson.print_column()* method to print out the first 10 columns.

#### Submission Instructions

Rename your file to `<firstname>-<lastname>-sqlperson.py` and upload it to Moodle.
