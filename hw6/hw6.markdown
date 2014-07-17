## Week 6 assignment

### Installing SQLite

To install SQLite 3 in Ubuntu, use the following command:

$ sudo apt-get install sqlite3

### Problem 1. SQLite from Command Line

- Grab the template:

#### Overview

In this problem, we will use the SQLite command line tool to perform some simple database tasks. There are two ways to use the SQLite command line tool. You can either simply do

    $ sqlite3 mydatabase.db
    SQLite version 3.8.5 2014-06-04 14:06:34
    Enter ".help" for usage hints.
    sqlite> 

which brings up the sqlite prompt, where you can interactively enter SQL commands line by line; or you can write an SQL script in text file format (e.g. `census.sql`), and run it from the command line with 

    $ sqlite3 mydatabase.db < census.sql

You might find it easier to practice and debug using the first option, but for submission, you will have to write an SQL script and make sure that the second method works.

#### Creating a new SQL database

Your first task is to create a new SQLite database from the Illinois census file. Although _sqlite_ can import CSV files, some pre-processing is still necessary. We will use the columns "SERIALNO", "SPORDER", "AGEP", "WKHP", and "PINCP". Most of these should be familar to you. "SERIALNO" is a unique serial number that identifies each household and "SPORDER" is an identifier that distinguishes each person in the household. Thus, when we combine these two numbers, we have a unique identifier for every person. This combination will serve as PRIMARY KEY in SQLite. Let's extract these columns and make a CSV file that can easily be imported by SQLite:

    $ sed 1d ss12pil.csv | awk -F, '{if($73 == ""){$73 = 0};print $2$3 "," $8 "," $73 "," $104}' > ss12pil_sql.csv

Now, in your SQL script, the first thing you should do is

- CREATE a new table named _myCensus_ with four columns.

All columns are integers, and the first column should be PRIMARY KEY.

Next, since _ss12pil.csv_ is still a CSV file, we have to tell SQLite that the file is separated by commans:

    sqlite> .separator ,
    sqlite> .import ss12pil_sql.csv myCensus

Note that you have to create a new table __before__ importing a CSV file. Above commands imports the CSV file into the _mycensus_ table.

#### Joining two databases

Grab the CSV file:

You have just finished creating an SQL database from the CSV file, but someone comes along and hands you another CSV file, *ss12pil_favorite_number.csv*. This file was created by going around and asking each person in the _ss12pil.csv_ file what his or her favorite single-digit number is. Note that the rows of the two files are not in the same order, i.e.

    $ head -3 ss12pil_sql.csv 
    3801,50,0,000121000
    3802,45,40,000027000
    3803,26,40,000020000
    $ head -3 ss12pil_favorite_number.csv 
    50995101,8
    131478101,2
    81532401,2

- Create a new table named _moreCensus_ with two columns. Import *ss12pil_favorite_number.csv*.

Now we want to join this newly created database *moreCensus* with the original database *myCensus*.

- JOIN (or INNER JOIN) _myCensus_ and _moreCensus_ by matching PRIMARY KEY. Combine them into a new table _myMoreCensus_.

#### Inserting

At this point, you decide for some reason that you may as well enter your own information into the database. 

- INSERT a new row into *myMoreCensus*. Assume that your PRIMARY KEY is 101, you are 21 years old, works 40 hours a week, makes one million dollars a year, and your favorite number is 1.

#### Query

Finally, do a query to find

- The number of individuals of 18 years of age or older who worked 40 hours or more per week, earned an annual income of more than $ 500,000, and whose favorite digit is 1.

The answer should be

    21504101,58,55,607000,1
    66592402,62,50,540000,1
    93004702,71,72,607000,1
    121640701,48,40,607000,1
    133309001,33,45,560000,1
    148470501,51,70,733000,1
    101,21,40,1000000,1

#### Submission Instructions

Make sure that your SQL script runs without a problem when you do

    $ sqlite3 mydatabase.db < census.sql

Rename your file to `<firstname>-<lastname>-census.sql` and upload it to Moodle.

### Problem 2. SQLite in Python

- Grab the template:

#### Overview

In this problem, you will repeat the same task in Problem 1 using the *sqlite3* library in Python. Note that the functions `read_my_census()`, `read_more_census()`, `join_census()`, and `insert_me` take an `sqlite3.Connection` object and return an `sqlite3.Connection` object. The fifth function `find_millionaires()` takes an `sqlite3.Connection` object and returns a `pandas.Dataframe` object.

#### Function: read_my_census()

- Use pandas.read_csv() and pandas.to_sql() functions to read the `ss12pil_sql.csv` file and convert it to an SQL database named _myCensus_.

#### Function: read_my_census()

- Use pandas.read_csv() and pandas.to_sql() functions to read the `ss12pil_favorite_number.csv` file and convert it to an SQL database named _moreCensus_.

#### Function: join_census()

The `join_census()` function joins _myCensus_ and _moreCensus_ tables into a new table. It is probably easiest to

- Use the same command from Problem 1 as an argument to the `execute()` method.

#### Function: insert_me()

This function inserts a new row into the `myMoreCensus` table. You should use the same values you used in Problem 1.

- Use the same command from Problem 1 as an argument to the `execute()` method.

#### Function: find_millionaires()

The `find_millionaires()` function takes an `sqlite3.Connection` object as an argument and returns a `pandas.Dataframe` object.

- Use `pandas.read_sql()` method to issue the same query as in Problem 1.

#### Function: main()

The _main_ function will create a `sqlite3.Connection` object, call each of above functions in turn, and print out the result. The final result should be

              id  age  hours_worked   income  favorite_number
    0   21504101   58            55   607000                1
    1   66592402   62            50   540000                1
    2   93004702   71            72   607000                1
    3  121640701   48            40   607000                1
    4  133309001   33            45   560000                1
    5  148470501   51            70   733000                1
    6        101   21            40  1000000                1

#### Submission Instructions

Rename your file to `<firstname>-<lastname>-sqlcensus.py` and upload it to Moodle.

### Problem 3.

- Grab the template:

#### Overview

In this problem, you will use a class object to interact with an SQL database. Make sure you read the section [SQLite and Python types](https://docs.python.org/3.4/library/sqlite3.html#sqlite-and-python-types) in the official Python documentation. This problem and the template file follow one of the sample code very closely, so read it very carefully.

Recall that in week 3 assignment you wrote a class named _OnePerson_ that represents a row in the Illinois census file. All you have to do in this problem is adapt the sample code in the above link to the _OnePerson_ object. Thus, you will need to import _person.py_ module you wrote. If you want to use your own code, you will have to make it possible to construct the class by passing a list, e.g.

    person = OnePerson(['a', 'b', 'c'])

that is, your initializer should be something like

    def __init__(self, row = None):
		self.row = row

If you are not sure your code will behave correctly, you can download my own version of [person.py]() from GitHub.

At the end, your code should perform exactly the same function as the code from week 3---read the 100th line of the census file and print out the first 10 columns.

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

Only this time, you will do this by interacting with an SQL database. As the official Python documentation explains, in order to move back and forth between Python and SQLite, we need an adaptor that sends the _OnePerson_ class to SQLite by representing the object as a string, and a converter that accepts the string representation and reconstructs a _OnePerson_ object.

#### Function: adapt_person()

- Write a function named *adapt_person()* that accepts a _OnePerson_ object as an argument and returns a string representation of _OnePerson.row_ (each item in the list separated by commans).

#### Function: convert_person()

- Write a function named *convert_person()* that accepts a list of strings and returns a *OnePerson* object constructed from this list.

#### Function: create_table()

- Write a function named *create_table()* that accepts an *sqlite3.Cursor* object and creates an SQL table named *myCensus*, which stores an instance of *OnePerson* object.

#### Function: insert_person()

- Write a function named *insert_person()* that accepts an *sqlite3.Cursor* object as the first argument and a *OnePerson* object as the second argument. It then inserts the values of *OnePerson* object into the *myCensus* table created by the *create_table()* function.

#### Function: print_head()

- Write a function named *print_head()* that accepts an *sqlite3.Cursor* object. It should first execute a SELECT statement that retrieves the instance of *OnePerson* object stored in the *myCensus* table. It should then call the cursor's *fechone()* or *fetchall()* to retrieve the *OnePerson* object. Use the *OnePerson.print_column()* method to print out the first 10 columns.

#### Submission Instructions

Rename your file to `<firstname>-<lastname>-sqlperson.py` and upload it to Moodle.
