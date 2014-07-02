## Week 5 Assignment

### Problem 1. Popular Baby Names

Grab the template file: [FirstName-LastName-babyname.py]()

In this problem, we will use Beautiful Soup to parse the [HTML page](http://www.ssa.gov/cgi-bin/namesbystate.cgi) for the most frequent baby names in 2013 in Illinois based on Social Security card application data.

Before you begin, install [Requests](http://docs.python-requests.org/en/latest/):

    $ sudo apt-get install python-requests

We will create a class named `BabyNames`, which must have at minimum the following:

- Attributes:
  `state` (str): Two-letter abbreviation of state.
  `year` (str): Year from 1960 to 2013.
  `fields` (list of strings): Headers of the table.

- Methods:
  `get_page`(self): Fetches the HTML page on SSA using Requests. Takes no argument and returns a string (unicode).
  `parse_page`(self, page): Uses Beautiful Soup to parse an HTML page fetched with get_page() method and converts it to pandas.DataFrame object. Takes a string (unicode) of concatenated HTML and returns pandas.DataFrame.

In the `get_page()` method, refer to [More Complicated POST requests] and

- Use `requests.post()` to make an HTTP request. Pass `query` to the `data` argument. Return `r.text`.

In order to the `parse_page()`, we need to first understand how the HTML page you want to parse is structured. In Chrome, I right-clicked on the web page and selected "Inspect Element" from the pop-up menu.

![inspect_element](babynames.png)

Your browser should have a similar method that shows the HTML source. Note in the figure that a row is surrounded by

    <tr align="right">...</tr>

and each column within that row is surrounded by

    <td>...</td>

- Use the [find_all()](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all) function to parse the HTML page and extract the fields `rank`, `male_name`, `number_of_males`, `female_name`, and `number_of_females`.

I think the easiest way is to use each field in `fields` as a keyword to a dictionary and store a list for each field. That is, we would have

    my_dict[u'rank'] = [u'1', u'2', ..., u'100']
	my_dict[u'male_name'] = [u'Noah', u'Alexander', ..., u'Jesus']

and so on (note that all strings are in unicode). This dictionary can easily be converted to a `pandas.DataFrame` by

    dataframe = pd.DataFrame.from_dict(my_dict)

The `parse_page()` method can then return this `dataframe`.

- Rename your file to `<firstname>-<lastname>-babynames.py` and upload it to Moodle.

### Problem 2. Simple Statistics Using Pandas.

Grab the template file: [FirstName-LastName-pdstats.py]()

In the previous weeks, we have seen different ways to read selected columns from the census CSV file and calculate basic statistics. In this problem, we will see how easy it is to perform the same task using Pandas. 

First, write a function named `read_census()` that takes the filename (string) as an argument and returns pandas.DataFrame.

- Use the [read_csv](http://pandas.pydata.org/pandas-docs/stable/io.html#io-read-csv-table) function in Pandas.
- Don't forget that "MARHT" and "WKHP" had empty fields, which should actually be zero. When you first create a DataFrame from the census data, you will notice that these empty fields are filled with NaN (Not a Number). Use [pandas.DataFrame.fillna()](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.fillna.html) to replace NaN with 0s.

Next, write a function named `get_stats()` that takes a Pandas DataFrame as the first argument and the column number (integer) as the second argument, and returns a tuple of minimum, maximum, mean, and median.

 - Use [pandas.DataFrame.min()](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.min.html), [pandas.DataFrame.max()](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.max.html), [pandas.DataFrame.mean()](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.mean.html), and [pandas.DataFrame.median()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.median.html)

Rename your file to `<firstname>-<lastname>-pdstats.py` and upload it to Moodle.

### Problem 3. Twitter Tag Cloud.

Grab the template file: [FirstName-LastName-twit.py]()

I got the idea for this problem while I was talking to Ola from our class and she mentioned [infographics](http://en.wikipedia.org/wiki/Infographic). So if this assignment turns out to be too difficult, you can blame her (thanks, Ola!). We will begin with a trending topic, fetch some tweets, and create a [tag cloud](http://en.wikipedia.org/wiki/Tag_cloud) such as this one created by searching for __#informatics__,

![cloud](cloud.png)

Before you begin, you need to install some third-party libraries. You might have had some trouble with `python-twitter` package in the apt-get repository. Uninstall this and use `pip install` instead:

    $ sudo apt-get purge python-twitter
    $ sudo pip install twitter

You should also install [PyTagCloud](https://pypi.python.org/pypi/pytagcloud) by doing:

    $ sudo apt-get install python-pygame python-simplejson
    $ sudo pip install pytagcloud

Next, create Twitter OAuth credientials and get API access at [https://dev.twitter.com/apps](https://dev.twitter.com/apps) as detailed in Chapter 1 of _Mining the Social Web 2nd Edition_ by Matthew A. Russell (hereafter refered to as simply the book). First, take a look at the template file and note that there is a function named `search_twitter`, a slight modification of the trending topics search routine of Example 1-5 in the book,

    search_twitter(twitter_api, q, search_size = 100, stop_count = 10000)

where twitter_api is the `twitter.api.Twitter` object, and `q` is the query string.

<!-- Be warned that calling this function too often will result in "rate limit exceeded" error from Twitter. You should probably save the function in a different file, import it as a module in IPython, and use that object to write and debug your code. That is, in your interpreter, do -->

<!--     >>> import twittercloud as tc -->
<!--     >>> auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET) -->
<!--     >>> twitter_api = twitter.Twitter(auth = auth) -->
<!--     >>> q = '#informatics' -->
<!--     >>> statuses = search_twitter(twitter_api, q) -->

<!-- and use `statuses` instead of calling `search_twitter` repeatedly. If this is too inconvient, you may simply write and debug as it is, but consider yourself warned that you can get locked out for an hour if you exceed the rate limit. -->

If you read the book, you know that `statuses` is a list of dictionaries that contains all the metadata from every tweets we fetched. You need to extract only the text data. And we also need to clean up the texts since they still contain special characters such as hashtags and @ signs, and HTTP links. Thus,

- Write a function named `clean_statuses()` that takes the above object `statuses` as an argument and returns a list of strings.

The `statuses` object is a list of dictionaries, so the texts we need are in the `statuses[0]['text']`, `statuses[1]['text']`, etc. You can use list comprehension to extract the texts and make a list named `status`. These texts will be UNICODE strings, and if you are using Python 2, you have to convert them to ASCII strings. You can do this by

    status = [s.encode('ascii', 'ignore') for s in status]

Next, we will use `re` regular expression operations to

- Split the text into words (words in a text are separated by whitespaces),

and remove all items in the list with the following:

- hashtags (#),
- users (@),
- links (begins with http), and
- words containing any non-alphabetical characters.

The easiest way to do this (that I can think of) is substituting the above matching pattern with empty strings `''`, and at the end, using list comprehension to remove all the empty strings from the list.

At this point, it might be a good idea to

- Convert everything remaining to lower cases.

Finally,

- Return the list of cleaned-up words.

Now returned from the `clean_statuses` function is a list of all the words we want. To create a tag cloud, we need the frequency of each word, because the size of each word in the tag cloud is determined by the frequency of the word.

We will use Pandas in a function named `get_counts()` to calculate the frequency of each word and return a list of tuple of the form (string, int). The `get_counts()` function takes a list of strings which we will call `words`.

- Create a [pandas.Series](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.Series.html) object from `words`.

- Use the `pandas.Series.values_count()` to calculate the frequency of each word. I'll call this returned object `counts`.

- To create a list of tuples from `counts`, you can use

        counts = [item for item in counts.iteritems()]

- Return this list of tuples (string, int).

Now, we are finally ready to use the third-party library _pytagcloud_ to create a tag cloud. I'll call the object returned from the `get_counts()` function `word_counts`.

    tags = make_tags(word_counts, maxsize = 120)
    create_tag_image(tags, 'cloud.png', size = (900, 600), fontname = 'Lobster')

This will create the tag cloud in the file `cloud.png`.

- Rename `<firstname>-<lastname>-twittercloud.py` and upload it to Moodle.
