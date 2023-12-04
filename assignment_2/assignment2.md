# Assignment 2: Data Management

## Introduction

In this assignment you will work on a small but realistic data management project. As
always, you will collaborate via git.

To avoid disappointments, here are a few rules for all tasks:

1. Write good commit messages and commit frequently. Use git for the entire process. Do
   not hesitate to commit unfinished or broken code. Git should be the only way to share
   code with your peers.
1. You only get points if you contribute. If you don't commit at all or your only commit
   trivial stuff (like fixing a typo in a comment) you will not get points, even if your
   group provides a good solution.
1. All functions need docstrings
1. Functions must not have side effects on inputs
1. Never overwrite the original data
1. Do not commit generated files (e.g. cleaned datasets)
1. Follow the rules for working with file paths
1. Use the "modern pandas" settings for all exercises

>

The deadline is **November 20, 11 pm**

The entire solution has to be in `.py` files. If you find it easier, you can prototype
some of the functions in jupyter notebooks. In that case, it is a good idea if each
group member has their own notebook, so you do not get merge conflicts.

## Background

In this assignment you will do data management for the paper *Estimating the Technology
of Cognitive and Noncognitive Skill Formation* by Cunha, Heckman and Schennach (CHS),
Econometrica, 2010.

Doing the complete data management of such a complicated project is not possible in one
assignment (it often takes weeks or months). Therefore, you will only work with a small
subset of the variables needed to replicate the paper. Moreover, we will save you some
of the most painful steps by providing a pre-processed version of the dataset and csv
files that will help you to harmonize variable names between panel waves.

We will focus on the Behavior Problem Index that is used to measure non-cognitive
skills. This index has the subscales antisocial behavior, anxiety, dependence,
headstrong, hyperactive and peer problems. Here is an
[overview](https://www.nlsinfo.org/content/cohorts/nlsy79-children/other-documentation/codebook-supplement/appendix-d-behavior-proble-0).

The assignment repository contains a file called `src/original_data/original_data.zip`,
with four files in it:

- `BEHAVIOR_PROBLEMS_INDEX.dta`: Contains the main data you will work with. It is in
  wide format and the variable names are not informative. Moreover, the names do not
  contain the survey year in which the question was asked.
- `bpi_variable_info.csv`: Contains information that will help you to decompose the main
  dataset into datasets for each year and to rename the variables such that the same
  questions get the same name across periods. In a real project you would have to
  generate this information yourself.
- `BEHAVIOR_PROBLEMS_INDEX.cdb`: The codebook of the dataset. If you have any questions
  about the data, the answers are probably in the codebook.
- `chs_data.dta`: The data file used in the original paper by Cunha Heckman and
  Schennach.

## Task 1

Follow [this link](https://classroom.github.com/a/78q9nXCM), create the repository for
your group and clone it to your computers.

## Task 2

Make sure you have seen the
[screencast](https://effective-programming-practices.vercel.app/pandas/functional/objectives_materials.html)
on functional data management and worked through the functional data management
[example](https://effective-programming-practices.vercel.app/pandas/functional/functional_pandas.html#functional-data-management-example).

Answer the following questions in your README file:

- In the
  [imperative way](https://effective-programming-practices.vercel.app/pandas/functional/functional_pandas.html#the-imperative-way)
  the DataFrame is changed in-place many times and variables of the same name changed
  their content. Describe why this is a problem, especially when working in a jupyter
  notebook.
- Read the code in the
  [functional way](https://effective-programming-practices.vercel.app/pandas/functional/functional_pandas.html#the-functional-way).
  Does any of the functions have a side effect on its inputs?
- The
  [functional way](https://effective-programming-practices.vercel.app/pandas/functional/functional_pandas.html#the-functional-way)
  contains three functions. One of them could be called the `main` function and the
  others are `helper` functions. Which one is the main function and why?

**Note**: It is a good idea to mark the helper functions by starting their name with an
underscore (`_`)

## Task 3

For this task you will work in `unzip.py` and store the results in the `bld` directory.

Use pathlib to check if the `bld` directory exists and create it otherwise.

Modify your `.gitignore` file to make sure that all files in the `bld` directory are
ignored.

Unzip the the file `src/original_data/original_data.zip`. This
[stackoverflow post](https://stackoverflow.com/questions/3451111/unzipping-files-in-python)
tells you how. Since the unzipped files are generated, they should not be under version
control.

## Task 4

For this task you will work in `clean_chs_data.py`

Implement the function `clean_chs_data.py`. The function should take a DataFrame and
return a DataFrame.

Use as many helper functions as you need. Give them good names and mark them as helper
functions by starting the name with an underscore.

The cleaned data should contain the following columns:

- "bpiA", "bpiB", "bpiC", "bpiD", "bpiE". They are cleaned versions of columns with the
  same name in the raw data. Cleaned means that missing are coded as pandas missings (NA
  or NaN) instead of negative numbers.
- The column "momid" based on the original column "momid". Choose a suitable dtype.
- "age", just copied over from the raw data. This is an integer as it was discretized to
  two year bins.

Set the index to \["childid", "year"\] and choose suitable dtypes for both index
variables

At the bottom of the py file you find an `if __name__ == '__main__'` clause. You can
watch a video on [why it's necessary](https://www.youtube.com/watch?v=g_wlZ9IhbTs) if
you want.

Add the code suggested by the comments inside the if condition.

For those who watched the video: You do not have to put everything you do inside the
condition into a main function. Putting multiple function calls into the if condition is
completely fine.

Don't forget to write docstrings for all functions. A one-liner is enough for helper
functions

## Task 5

For this task you will work in `clean_nlsy_data.py`.

Implement the function `clean_year_data`. The function takes the entire raw nlsy
dataset, a year (between 1986 and 2010, both inclusive and only even year numbers) and
the bpi variable info (as a DataFrame).

It returns a DataFrame with the cleaned data of the requested year.

Use as many helper functions as you need. Give them good names and mark them as helper
functions by starting the name with an underscore.

The cleaned data should contain the following variables:

- Clean versions of all variables that make up the
  [BPI](https://www.nlsinfo.org/content/cohorts/nlsy79-children/other-documentation/codebook-supplement/appendix-d-behavior-proble-0).
  They have an ordered categorical dtype with the values "not true" \< "sometimes true"
  \< "often true". The variables have the name indicated in the bpi_variable_info file.
  Missings are coded as pandas missings (NA or NaN) instead of negative numbers. The
  dataset contains surprises such as variables that take values you did not expect or
  category labels that are similar but not identical across variables. Try to find good
  solutions for each of them.
- Scores for each subscale of the behavioral problems index (bpi) that are calculated by
  averaging the items of that subscale. Before averaging, you need to convert the
  categorical variables to numbers. For this, the answers 'sometimes true' and 'often
  true', are counted as 1; 'not true' is counted as 0. Use the names "antisocial",
  "anxiety", "headstrong", "hyperactive", "dependence" and "peer".

Set the same index as for the chs_data.

Don't forget to write docstrings for all functions. A one-liner is enough for helper
functions

## Task 6

You continue to work in `clean_nlsy_data.py`

Implement the function `clean_and_reshape_nlsy_data`. This function takes the entire raw
nlsy dataset and variable info as DataFrames. It calls `clean_year_data` to create a
list of cleaned yearly datasets and concatenates them into one DataFrame in long format.

Only keep the data for **even years** between 1986 and 2010.

As before, add data loading and function calls in the `if __name__ == '__main__`
condition.

## Task 7

For this task you will work in `merge.py`.

Merge the clean chs data with the clean nlsy data. Only keep observations that are
present in the chs data. Before you merge, check that there are no overlaps in column
names between the two datasets.

Restrict the merged data sets to the age groups 5 to 13 (both inclusive)

Use an `if __name__ == '__main__'` condition for all function calls.

## Task 8

For this task you will work in `plot.py`

You will plot your scores against the ones in the chs data -- for each score and age.

Make a grid of [regression plots](https://plotly.com/python/ml-regression/) for each
score that show how your score relates to the corresponding score in the chs data. Each
grid contains 5 subplots, one for each age group.

**Note**: Making such grids is really easy in plotly. Search for the word `facet` in the
documentation of
[`px.scatter`](https://plotly.com/python-api-reference/generated/plotly.express.scatter.html)

The names of their score relate to your names as follows:

```python
{
    "antisocial": "bpiA",
    "anxiety": "bpiB",
    "headstrong": "bpiC",
    "hyperactive": "bpiD",
    "peer": "bpiE",
}
```

The dependence scale has no counterpart in the chs data. If you did everything correctly
you should see a perfectly negative correlation for some variables and a strong but not
perfectly negative correlation for other variables.

Save the plots under suitable file names in the `bld` folder. `.png` is the preferred
format. If you are on Windows and have trouble to export static plotly plots (even with
the workaround) you can switch to `.html` instead.

Use an `if __name__ == '__main__'` condition for all function calls.
