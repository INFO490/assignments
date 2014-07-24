## Week 7 Assignment

### Problem 1. PMF, CDF, and CCDF.

- Grab the template: [distributions.py](https://github.com/INFO490/assignments/blob/master/hw7/distributions.py)

#### Overview

In this problem, you will compute probability mass function (PMF), cumulative distribution function (CDF), and complementary cumulative distribution function (CCDF), and plot them. Here are the examples to show where we are going. First, we plot the PMF of the WKHP column (hours worked per week) of *ss12pil.csv*.

![pmf](pmf_work.png)

Predictably, most people work 40 hours a week. Next, we plot the CDF of the PINCP (income) column,

![cdf](cdf_log_income.png)

and also plot the CCDF,

![ccdf](log_ccdf_log_income.png)

These two plots tell us a lot about the income distribution. First, note that the CDF of log(income) is that of a normal distribution (see Figure 4.5 in *Think Stats* by Allen B. Downey). Thus, it suggests that the income distribution is a log-normal distribution. Second, the log-log plot of CCDF looks like a log-normal distribution for the most part, but it becomes a straight line in the very high-income region (The jaggedness is due to the small sample size in this region). If you have read Section 4.2 of *Think Stats*, you know that the CCDF of a [Pareto distribution](http://en.wikipedia.org/wiki/Pareto_distribution) looks like a straight line on a log-log scale. So which one is it, log-normal or Pareto, or could it be both at the same time?

According to Wikipedia on [log-normal distribution](http://en.wikipedia.org/wiki/Log-normal_distribution),

> In economics, there is evidence that the income of 97%–99% of the population is distributed log-normally. (The distribution of higher-income individuals follows a Pareto distribution.)

It seems like we have (or are about to) reproduce just such evidence. The major tasks in this problem are:

- Write *get_histogram()* function,
- Write *get_pmf()* function,
- Write *get_cdf()* function, (CCDF is simply 1.0 - CDF)
- Plot PMF of hours worked per week,
- Plot CDF of income,
- Plot CCDF of income.

#### Function: get\_histogram()

- Write a function named *get_histogram()* that takes a list and returns a dictionary of the form {value: frequency}.

As the name suggests, this function returns the dictionary form of a histogram. See Section 2.3 of *Think Bayes* for hints.

#### Function: get\_pmf()

- Write a function named *get_pmf()* that takes a list and returns a dictionary of the form {value: probability}.

Note that PMF is a *normalized* histogram, and you may want to call *get_histogram()* function from inside *get_pmf()* function. See Section 2.3 of *Think Bayes* for hints.

#### Function: get\_cdf()

- Write a function named *get_cdf()* that takes an array *sequence* and returns a tuple that represents the x and y axes of the (empirical) CDF.

Here is a very easy algorithm to implement this function. See the definition of [empirical distribution function](http://en.wikipedia.org/wiki/Empirical_distribution_function) on Wikipedia. That means we can simply

1. First, sort the *sequence* array. This will be our x-axis,
2. Next, make an array of [1 / N, 2 / N, ..., 1]. This will be our y-axis. All you have to do is use *np.arange()* to make an array of the same length as the *sequence* array, and divide it by the length of *sequence*.

According to Wikipedia, the resulting empirical CDF is an unbiased estimator for the true CDF.

#### Function: main()

In the *main()* function, you have to use *Matplotlib* to plot similar figures to the ones shown above. Note that we import *get_columns* function from [stats2.py](https://github.com/INFO490/assignments/blob/master/hw7/stats2.py) module that we wrote in week 3, so if you are not sure if your *get_columns* function is written correctly, download both [stats2.py](https://github.com/INFO490/assignments/blob/master/hw7/stats2.py) and [stats.py](https://github.com/INFO490/assignments/blob/master/hw7/stats.py).

#### Submission instructions

- Rename your file to `<firstname>-<lastname>-households.py` and upload it to Moodle.

### Problem 2. The Locomotive Problem.

- Grab the template: [households.py](https://github.com/INFO490/assignments/blob/master/hw7/households.py)

#### Overview

The locomotive problem is found in Section 3.2 of *Think Bayes* by Allen B. Downey. We will rephrase the locomotive problem and apply it to our Illinois census data:

> The households in 2012 Illinois census data are labeled using the serial numbers {1, ..., N}. You see a household with the serial number 1493780. Estimate how many households there are in Illinois.

The number 1493780 is the serial number of the very last household in the *ss12pil.csv* file.

However, we will completely rewrite Downey's code by eliminating the class structure and using Numpy, because

1. Classes have their advantages, but they make it hard to see what is really going on under the hood, and our goal in this problem is to understand the underlying concepts,
2. Using Numpy means no *for* loops, which in my opinion makes it easier to understand what's going on,
3. Downey mostly uses pure Python. This is very slow, so we will use Numpy. The difference in speed may not matter much when we are dealing with a locomotive with the serial number 60 and a total number of locomotives on the order of thousands. But when the serial number is close to 1.5 million and the total number could be on the order of tens of millions, the difference in speed is substantial.

How substantial is the difference? Applying Downey's pure Python code to our problem, I got

    $ time python train.py
    Estimated number of households: 5285183

    real    0m24.686s
    user    0m18.316s
    sys     0m0.928s

but using Numpy, I got

    $ time ./households.py 
    Estimated number of households: 5285183

    real    0m0.963s
    user    0m0.568s
    sys     0m0.392s

And that's for one serial number. When you run Bayesian updates for example, the difference quickly adds up.

Your task is to write the following five functions:

- get\_hypotheses()
- get\_uniform_prior()
- get\_likelihood()
- get\_posterior()
- get\_estimate()

Note that if you use Numpy functions correctly, each function should not take more than one or two lines to write. I will give you hints on how to do this, but you don't have to follow my recommendations as long as your functions do what they are supposed to do, i.e. take the specified parameters and return the correct Numpy arrays. But remember that all functions must return Numpy arrays, so if you use *for* loops you code will be very inefficient.

#### main

The main function is already written and provided for you. You don't have to write anything here. Browse this first to understand the big picture.

#### Function: get\_hypotheses()

- Write a function named *get_hypotheses()* that takes two integers (the first serial number 1 and the final serial number N) and returns a Numpy array of integers [1, 2, ..., N].

Note that the number N will be used for building a uniform prior. So what is our prior belief regarding the number of households in IL before seeing the data? Not much except that we have some idea about the population of IL. A quick google search shows me that the population of IL in 2012 was 12.88 million. The number of households cannot be greater than the population, so it would be reasonable to use a hypotheses of [1, 2, ..., 12880000].

Hint: See [numpy.arange()](http://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html).

#### Function: get\_uniform_prior()

- Write a function named *get_uniform_prior()* that takes a Numpy array (an array of hypotheses) and returns a Numpy array of floats (an array of uniform prior).

The prior is P(H) in Bayes' theorem. It is uniform, i.e. all elements in the array have same values, 1 / N.

Hint: See [numpy.ones_like()](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ones_like.html). Create an array of same length as *hypotheses* with all ones (you probably want floats). Divide all elements by the length of *hypotheses*.

#### Function: get\_likelihood()

- Write a function named *get_likelihood()* that takes an integer (data) and a Numpy array (hypotheses), and returns a Numpy array of floats (likelihood).

The likelihood is P(D|H) in Bayes' theorem. Remember that hypotheses is a Numpy array of [1, 2, ..., N]. If the n-th element of hypotheses is smaller than data, the likelihood is zero because the serial number cannot be greater than the number of households. On the other hand, if the n-th element of hypotheses is greater than or equal to data, the question becomes what is the chance of getting a particular serial number given that there are hypotheses[n] persons? Thus, if hypotheses[n] >= data, we return 1 / hypotheses[n], and 0 otherwise.

Hint: Say you have the following Numpy arrays:

    >>> x = np.array([1.0, 2.0, 3.0])
    >>> y = np.array([0.5, 2.5, 2.5])

You want to compare them *element-wise* and create a Boolean array of True if x >= y and False if x < y. An easy way to do this is

    >>> (x > y)
    array([ True, False,  True], dtype=bool)

See also [numpy.ndarray.astype()](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.astype.html). That means we can convert our Boolean array to, say, an array of floats with

    >>> (x > y).astype(np.float)
    array([ 1.,  0.,  1.])

#### Function: get\_posterior()

- Write a function named *get_posterior()* that takes an integer (data) and a Numpy array (hypotheses), and returns a Numpy array of floats (posterior).

From Bayes' theorem, the posterior P(D) is equal to prior times likelihood (divided by normalizing constant). Thus, the *get_posterior()* function should call *get_uniform_prior()* using *hypotheses*, call *get_likelihood()* using *data* and *hypotheses*, and multiply them to produce a posterior.

Hint: A simple multiplication of two Numpy arrays performs the multiplication *element-wise*. For example,

    >>> x = np.array([1.0, 2.0, 3.0])
    >>> y = np.array([4.0, 5.0, 6.0])
    >>> x * y
    array([  4.,  10.,  18.])

This element-wise multiplication is exactly what we want; we want to multiply the prior and the likelihood element-wise.

Hint: Don't forget to normalize. Since adding up all elements of the posterior array should give you 1.0, an easy way to normalize is to divide each element by the sum of all elements. See [numpy.sum()](http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html). For example, 

    >>> x = np.array([1.0, 2.0, 3.0, 4.0])
    >>> x / x.sum()
    array([ 0.1,  0.2,  0.3,  0.4])

#### Function: get\_estimate()

- Write a function named *get_estimate()* that takes a two Numpy arrays (posterior and hypotheses) and returns a Numpy array of floats (estimate).

Hint: Again, you can use element-wise multiplication of *hypotheses* and *posterior*, and our estimate is the sum of all elements in the product array.

#### Submission instructions

- Rename your file to `<firstname>-<lastname>-households.py` and upload it to Moodle.

### Problem 3. Least Squares Fit.

- Grab the template: [lsqfit.py](https://github.com/INFO490/assignments/blob/master/hw7/lsqfit.py)

#### Overview

Using the Illinois census data *ss12pil.csv*, pick two columns that you believe will have a correlation, and compute a least squares fit for the two columns. Make a scatter plot of the two columns you chose. In the same figure, plot the line of best fit using the slope and intercept from the least squares fit. Submit your code via Moodle as *firstname-lastname-lsqfit.py*. Here's an example:

![lsqfit](lsqfit.png)

Section 9.6 of *Think Stats* describes how to compute a least squares fit, which I paraphrase:

<blockquote>
<p>Given two Numpy arrays x and y,</p>
<p>1. Compute the sample means, x.mean and y.mean, the variance of x, and the covariance of x and y.</p>
<p>2. The estimated slope is beta = Cov(x, y) / Var(x).</p>
<p>3. And the intercept is alpha = y.mean - beta * x.mean</p>
</blockquote>

You can find everything you need in [Numpy statistics functions](http://docs.scipy.org/doc/numpy/reference/routines.statistics.html).

#### Function: get\_lsqfit()

Your task is to use Numpy functions to

- Write a function named *get_lsqfit()* that takes two Numpy arrays and returns a tuple of two floats (slope and intercept).

Numpy already has a [function](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.lstsq.html) that does this, but you may __not__ use this function (or any other pre-built functions) in this problem. But it would be a good idea to compare your result with the Numpy least squares fit function to make sure that you got it right.

If you are going to use the *numpy.var()* function, you want to specify an optional parameter *ddof*, i.e. use `numpy.var(ddof = 1)`. See Numpy manual and Section 8.2 of *Think Stats* for discussion on biased and unbiased estimators.

#### Function: main()

- Create a scatter plot, and
- Use *alpha* and *beta* values to plot the line of best fit in the same figure.

Here are some tips:

- I used columns WKHP and PINCP, but you do not have to use the same columns I did. Or you can choose to reproduce the above plot. Your choice.

- The file *ss12pil.csv* is one of the American Community Survey (ACS) Public Use Microdata Sample (PUMS) files. You can read more about ACS PUMS [here](http://www.census.gov/acs/www/data_documentation/public_use_microdata_sample/). This [link](http://www.census.gov/acs/www/Downloads/data_documentation/pums/DataDict/PUMSDataDict12.pdf) is a pdf file of the data dictionary, which shows what each column (e.g. SERIALNO, AGEP, WKHP, etc.) means.

- For making scatter plots using Matplotlib, refer to week 4 lessons and Section 9.4 of *Think Stats*.

#### Submission instructions

- Rename your file to `<firstname>-<lastname>-lsqfit.py` and upload it to Moodle.
