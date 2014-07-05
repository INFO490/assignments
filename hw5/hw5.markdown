## Week 5 Assignment

### Problem 1. Popular Baby Names

#### Introduction

Grab the template file: [babynames.py](https://github.com/INFO490/assignments/blob/master/hw5/FirstName-LastName-babynames.py)

In this problem, we will use Beautiful Soup to parse the [HTML page](http://www.ssa.gov/cgi-bin/namesbystate.cgi) for the most frequent baby names in 2013 in Illinois based on Social Security card application data.

Before you begin, install [Requests](http://docs.python-requests.org/en/latest/):

    $ sudo apt-get install python-requests

We will create a class named `BabyNames`, which must have at minimum the following:

- Attributes:
 <p><code>state</code>(str): Two-letter abbreviation of state,</p>
 <p><code>year</code>(str): Year from 1960 to 2013,</p>
 <p><code>fields</code>(list of unicode strings): Headers of the table.</p>

- Methods:
 <p><code>get_page(self)</code>: Fetches the HTML page on SSA using Requests. Takes no argument and returns a string (unicode),</p>
 <p><code>parse_page(self, page)</code>: Uses Beautiful Soup to parse an HTML page fetched with get_page() method. Takes a unicode string of concatenated HTML and returns a dictionary of the form {fields: [column values]}.</p>

#### main

The `__main__` part is already written for you. You don't have to change anything here. Study this first to get the big picture. We create our object, fetch the HTML page, parse it, then display the top 5 baby names to make sure that we got it right.

	Top 5 baby names for IL, 2013
	Females: Olivia(881), Sophia(851), Emma(786), Isabella(671), Emily(558)
	Males: Noah(757), Alexander(728), Jacob(728), Liam(722), Michael(695)

#### Constructor

The `fields` attribute is already defined for you. There are two more attributes: `state` and `year`. Initialize them.

#### Function: get_page()

In the `get_page()` method, refer to [More Complicated POST requests](http://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests) and

- Use `requests.post()` to make an HTTP request. Pass `query` to the `data` argument. Return `r.text`.

#### Function: parse_page()

For the function `parse_page()`, we need to first understand how the HTML page you want to parse is structured. In Chrome, I right-clicked on the web page and selected "Inspect Element" from the pop-up menu.

![inspect_element](babynames.png)

Your browser should have a similar method that shows the HTML source. Note in the figure that a row is surrounded by `<tr align="right">...</tr>` and each column within that row is surrounded by `<td>...</td>` or `<td align="center">...</td>`.

- Use the [find_all()](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all) function to parse the HTML page and extract the columns `rank`, `male_name`, `number_of_males`, `female_name`, and `number_of_females`.

Note that all strings in this problem will be unicode strings (Python type `unicode`). Since parsing the HTML source gives us unicode strings, it is easier to make everything unicode including the dictionary keys.

Study the examples in the template. When you use one of the elements in the `self.field` attribute as a dictionary key, you should get the corresponding column in the table. (I hope this is intuitive and makes sense.)

#### Submission Instructions

- Rename your file to `<firstname>-<lastname>-babynames.py` and upload it to Moodle.

### Problem 2. Simple Statistics Using Pandas.

#### Introduction

Grab the template file: [pdstats.py](https://github.com/INFO490/assignments/blob/master/hw5/FirstName-LastName-pdstats.py)

In the previous weeks, we have seen different ways to read selected columns from the census CSV file and calculate basic statistics. In this problem, we will see how easy it is to perform the same task using Pandas. Remember, the purpose of this problem is to let you experience how easy it is to make a data table using Pandas. Don't overthink it.

#### Function: read_census()

First, write a function named `read_census()` that takes the filename (string) as an argument and returns pandas.DataFrame.

- Use the [read_csv](http://pandas.pydata.org/pandas-docs/stable/io.html#io-read-csv-table) function in Pandas.
- Don't forget that "MARHT" and "WKHP" had empty fields, which should actually be zero. When you first create a DataFrame from the census data, you will notice that these empty fields are filled with NaN (Not a Number). Use [pandas.DataFrame.fillna()](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.fillna.html) to replace NaN with 0s.

#### Function: get_stats()

Next, write a function named `get_stats()` that takes a Pandas DataFrame as the first argument and the column key (str) as the second argument, and returns a tuple of minimum, maximum, mean, and median.

 - Use [pandas.DataFrame.min()](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.min.html), [pandas.DataFrame.max()](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.max.html), [pandas.DataFrame.mean()](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.mean.html), and [pandas.DataFrame.median()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.median.html)

#### main

This part is all written for you. You don't have to change anything here.

#### Submission instructions

- Rename your file to `<firstname>-<lastname>-pdstats.py` and upload it to Moodle.

### Problem 3. Twitter Tag Cloud.

#### Introduction

Grab the template file: [twittercloud.py](https://github.com/INFO490/assignments/blob/master/hw5/FirstName-LastName-twittercloud.py)

I got the idea for this problem while I was talking to Ola from our class and she mentioned [infographics](http://en.wikipedia.org/wiki/Infographic). So if this assignment turns out to be too difficult, you can blame her (thanks, Ola!). Don't worry, because the bulk of the code is already written and provided for you, and you only have to write two functions (`clean_statuses()` and `get_counts()`). We will begin with a trending topic, fetch some tweets, and create a [tag cloud](http://en.wikipedia.org/wiki/Tag_cloud) such as this one created by searching for __#informatics__ (I think I see Champaign in there),

![cloud](cloud.png)

Before you begin, you need to install some third-party libraries. You might have had some trouble with `python-twitter` package in the apt-get repository. Uninstall this and use `pip install` instead:

    $ sudo apt-get purge python-twitter
    $ sudo pip install twitter

You should also install [PyTagCloud](https://pypi.python.org/pypi/pytagcloud) by doing:

    $ sudo apt-get install python-pygame python-simplejson
    $ sudo pip install pytagcloud

#### Function: main()

After installing the required packages, open up the template and take a look at the `main()` function. You have to get Twitter OAuth credientials and get API access at [https://dev.twitter.com/apps](https://dev.twitter.com/apps) as detailed in Chapter 1 of _Mining the Social Web 2nd Edition_ by Matthew A. Russell (hereafter refered to as simply the book), and fill in your OAuth credentials in place of the empty strings.

The rest of the `main()` function is already written for you, and you don't have to do anything here, although I encourage you to spend some time to understand the big picture.

#### Function: search_twitter()

Next, note that there is a function named `search_twitter()`. It is a slight modification of the trending topics search routine of Example 1-5 in the book,

    search_twitter(twitter_api, q, search_size = 100, stop_count = 1000)

where `twitter_api` is the `twitter.api.Twitter` object, and `q` is the query string. You don't have to change anything in this function.

#### Function: clean_statuses()

If you read the book, you know that `statuses` returned from `search_twitter()` function is a list of dictionaries that contains all the metadata from every tweets we fetched. We need to extract only the text data. We also need to clean up the texts since many of them contain non-alphabetical characters as well as special characters such as hashtags and @ signs, and HTTP links. Thus,

- Write a function named `clean_statuses()` that takes a list of dictionaries containing tweet metadata as an argument, and returns a list of strings.

The argument `statuses` is a list of dictionaries, so the texts we need are in `statuses[0]['text']`, `statuses[1]['text']`, etc. We can extract the texts and make a list named `status_texts` by writing

    status_texts = [status['text'] for status in statuses]

These texts will be UNICODE strings, and if you are using Python 2, you have to convert them to ASCII strings. You can do this by

    status_texts = [text.encode('ascii', 'ignore') for text in status_texts]

If you are not familiar with these syntaxes, these are called [list comprehensions](http://lmgtfy.com/?q=python+list+comprehension). These two lines are already in the template so you don't have to write them again.

Now your job is to write the rest of this function by using `re` regular expression operations to

- Split the text into words (words in a text are separated by whitespaces),

and remove all words that contain the following:

- hashtags (#),
- users (@),
- links (begins with http), and
- any non-alphabetical characters.

The easiest way to do this (that I can think of) is substituting any word that matches the above patterns with empty strings `''` (using regular expressions, or regex for short), and at the end, using list comprehension to remove all the empty strings from the list.

At this point, it might be a good idea to

- Convert everything to lower cases (this will make the tag cloud prettier in my opinion).

Finally,

- Return the list of cleaned-up words.

If you are confused about anything, you can simply google e.g. "python convert string to lowercases" or ask us questions.

#### Function: get_counts()

Now, returned from the `clean_statuses()` function is a list of nicely cleaned-up lowercase words. To create a tag cloud, we need the frequency of each word, because the size of each word in the tag cloud is determined by the frequency of the word.

However, our third-party library _PyTagCloud_ needs a list of tuples of the form (word, frequency) in order to create a tag cloud. Thus, we will write a function named `get_counts()` to calculate the frequency of each word and return a list of tuple of the form (string, int). Using Pandas makes the job easy, so

- Create a [pandas.Series](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.Series.html) object from a list of a list of strings `words`.

- Use `pandas.Series.values_count()` to calculate the frequency of each word. I'll call this returned object `counts`.

- To create a list of tuples from `counts`, you can use

        counts = [item for item in counts.iteritems()]

- Return this list of tuples (string, int).

#### Back to main()

Now, we are finally ready to use the third-party library _PyTagCloud_ to create a tag cloud. I'll call the object returned from the `get_counts()` function `word_counts`.

    tags = make_tags(word_counts, maxsize = 120)
    create_tag_image(tags, 'cloud.png', size = (900, 600), fontname = 'Lobster')

This will create the tag cloud in the file `cloud.png`. Open it up,

    $ xdg-open cloud.png

and see how pretty it is.

#### Submission Instructions

- Rename `<firstname>-<lastname>-twittercloud.py` and upload it to Moodle.
