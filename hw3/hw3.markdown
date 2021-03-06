## Week 3 Assignment

### Submission instructions

When you are ready to submit your work for grading, make sure that the name of your file is in `<firstname>-<lastname>-<projectname>.py` format, and submit your assignment as separate `.py` files in the Workshop. To get a full credit for this week's assignment you must upload three files:

 - `<firstname>-<lastname>-stats2.py`
 - `<firstname>-<lastname>-person.py`
 - `<firstname>-<lastname>-npstats.py`

Please use the provided template files and do not change the function names.

### Problem 1. Simple statistics revisited.

- Grab the template file: [stats2.py](https://github.com/INFO490/assignments/blob/master/hw3/FirstName-LastName-stats2.py).

This problem is a continuation of problem 3 from last week's assignment. Recall that you wrote a function named `get_stats()` that takes a list and returns a tuple of minimum, maximum, mean, and median. To use this function, rename your `.py` file from problem 3 to `stats.py` and import it as a module:

        from stats import get_stats

In case you couldn't write this function, you can use my version of [stats.py](https://github.com/INFO490/assignments/blob/master/hw3/stats.py) on GitHub.

We will use this function to compute basic statistics of the same four columns we extracted from the Illinois census data `ss12pil.csv` in week 1. Namely, we will use the following columns:

- Column 7, "PWGTP": the integer weight of each person,
- Column 8, "AGEP": the person's age,
- Column 40, "MARHT": the number of times married, and
- Column 73, "WKHP": the usual hours worked per week past 12 months,

where the first column is column 1 (rather than 0). Note that "MARHT" and "WKHP" columns have empty fields (which you should be able to check with `awk` command). The empty fields correspond to zero, so you have to devise a way to replace all `''`s with integer 0.

To extract these columns from the CSV file,

- Write a function named `get_column(filename, n, header = True)` that reads the `n`-th column from a file and returns a list of integers.

You may assume that the column is made of integers. We will also use the optional argument `header` because the first line of our file lists the names of the columns, but we might want to turn this off to handle a file that doesn't have a header.

- Use a combination of `with` statement and `open()` function to open `filename` in the `get_column()` function.
- Skip the first line if the `header` parameter is `True`; do not skip if it's `False`.
- If the `n`-th column is blank, assume it is 0.

We also want to print out the results in a nicely formatted manner.

- Write a function named `print_stats(input_list, title = None)`

that takes a list of integers and prints out the basic statistics, e.g.

        >>> print_stats([1, 2, 3, 4, 5], title = 'Title')
        Title
        Minimum: 1
        Maximum: 5
        Mean: 3.0
        Median: 3.0

- Use the imported `get_stats()` function inside the `print_stats()` function to calculate the statistics of `input_list` and print them out.

If the `get_stats()` function you wrote cannot handle <b>un</b>ordered lists, you have to first sort the `input_list` using `sort()` method or `sorted()` before passing it to `get_stats()`.

In the `main()` function,

- Use `get_column()` to extract the weight, age, number of times married, and usual hours worked per week of every person in the Illinois census data.
- Use `print_stats()` to print out the minimum, maximum, mean, and median of the four columns,

and finally,

- Rename `<firstname>-<lastname>-stats2.py` and upload it to Moodle.

### Problem 2. Using a class to represent an individual person.

- Grab the template file: [person.py](https://github.com/INFO490/assignments/blob/master/hw3/FirstName-LastName-person.py).

Each row in the census data represents an individual person. Classes are a great way to represent this. Thus, we will create a class named `OnePerson` to represent an individual person (one row in the census file). The `OnePerson` class should have at minimum the following:

- Attributes:  
  `row` (a list that represents a person)
- Methods:  
  `__init__(self)` (the usual initializer),  
  `read_line(self, input_file, n)` (reads the specified row from the input file),  
  `print_column(self, n)` (prints out the specified column)

In the `read_line()` method,

- Use a combination of `with` statement and `open()` function to open the `input_file`,
- Find the `n`-th line,
- Store that line in the `row` attribute as a list,

In the the `print_column()` method,

- print out the column number `n` and the value contained in that column.

In the `main()` function,

- Create an object named `person` using the `OnePerson` class.
- Use the `read_line()` method to read the 100th line of the census file.
- Use the `print_column()` method (in a loop) to print out the first 10 columns.

The output should be

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

- Rename `<firstname>-<lastname>-person.py` and upload it to Moodle.

### Problem 3. Simple statistics using Numpy.

- Grab the template file: [npstats.py](https://github.com/INFO490/assignments/blob/master/hw3/FirstName-LastName-npstats.py).

In this problem, you will reproduce the results of problem 1 using NumPy. First, you should get familiar with `numpy.loadtxt()`. In IPython, use the help magic function,

        In [1]: import numpy as np

        In [2]: np.loadtxt?

or read [this webpage](http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html).

- Write a function named `get_columns()` that takes the name of the file as the argument and returns a two-dimensional array of columns 6, 7, 39, and 72 (counting from 0).

You will need to set the following parameters:

- `delimiter`
- `converters`
- `skiprows`
- `usecols`
 
Do you remember from problem 1 that some columns had empty fields, which should actually be zero? The way to deal with missing values in `numpy.loadtxt()` is to set the `converters` parameter using [lambda functions](https://docs.python.org/2/reference/expressions.html#lambda):

        converters = {39: lambda x: float(x or 0), 72: lambda x: float(x or 0)}

As in problem 1, you should write a `print_stats()` function, but this time,

- Use NumPy methods: [numpy.min() or numpy.amin()](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.min.html), [numpy.max() or numpy.amax()](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.max.html), [numpy.mean()](http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html), and [numpy.median()](http://docs.scipy.org/doc/numpy/reference/generated/numpy.median.html).

In the `main()` function,

- use `get_columns()` and `print_stats()` to produce the statistics of weight, age, number of times married, and usual hours worked per week, with the same format from problem 1,

and fianlly,

- Rename `<firstname>-<lastname>-npstats.py` and upload it to Moodle.

Why use NumPy? In addition to providing useful mathematical functions, NumPy is much faster than pure Python. In IPython, you can determine how long a process takes to complete with `%time` or `%timeit`, or in the Unix environment, you can simply do

        $ time ./stats2.py

        real    0m17.453s
        user    0m16.640s
        sys     0m0.492s

        $ time ./npstats.py

        real    0m8.560s
        user    0m8.276s
        sys     0m0.252s

For the task of calculating basic statistics of four columns in a CSV file with 127k rows, NumPy is twice as fast as pure Python on my computer.
