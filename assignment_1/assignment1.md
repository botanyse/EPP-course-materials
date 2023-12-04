# Assignment 1: Python and Git

## Introduction

In this assignment you will collaborate via git and practice writing Python code. A
particular focus is on defining Python functions.

To avoid disappointments, here are a few rules for all tasks:

1. Stick to the exact file and function names mentioned in the tasks
1. Stick to the exact function signatures and behaviors mentioned in the tasks
1. Write good commit messages and commit frequently
1. You only get points if you contribute. If you don't commit at all or your only commit
   trivial stuff (like fixing a typo in a comment) you will not get points, even if your
   group provides a good solution.
1. All functions need docstrings (you will learn below what that means)
1. Functions must not have side effects on inputs

The deadline is **November 7, 11 pm**

## Task 1

Follow [this link](https://classroom.github.com/a/xnmOLruN), create the repository for
your group and clone it to your computers.

## Task 2

From basic Microeconomics you know the Cobb Douglas production function:

$$y = a \cdot x_{1}^{\gamma_1} x_{2}^{\gamma_2}$$

You have also seen the Leontief production:

$$y = a \cdot min\{x_1, x_2\}$$

And the CES function:

$$y = a \left (\gamma_1 x_1^{-\rho} + \gamma_2 x_2^{-\rho} \right )^{-\frac{1}{\rho}}$$

- create a file called `production_standalone.py` in which you will work for the
  remainder of the task.
- Implement the functions `cobb_douglas`, `leontief` and `ces`
- Use `x1`, `x2`, `gamma1`, `gamma2`, `a` and `rho` as variable names

## Task 3

At the bottom of `production_standalone.py`, create some test inputs for your functions
and evaluate the functions with those inputs.

You can choose the values for parameters and inputs. Pick values that make it easy to
calculate the correct result with pen and paper.

Add well formatted print statements that show that your functions work, i.e. when
executing `production_standalone.py` I want to see for each function what value it
returns and what the correct value is.

## Task 4

Write docstrings for all your functions and follow the
[google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
for docstrings.

Here is an example docstring for the cobb douglas function:

```python
def cobb_douglas(x1, x2, gamma1, gamma2, a):
    """Calculate the output of a Cobb-Douglas production function.

    Args:
        x1 (float): First input factor
        x2 (float): Second input factor
        gamma1 (float): First exponent
        gamma2 (float): Second exponent
        a (float): Total factor productivity

    Returns:
        float: The output of the Cobb-Douglas production function

    """
```

**From now on you need to write docstrings for every function you define in this
class!**

## Task 5

Split the content of `production_standalone.py` into two files:

`production_functions.py` contains all function definitions. `production_evaluations.py`
imports the functions from `production_functions.py` and contains the rest of the code
(function calls and print statements).

Write one paragraph in the file `README.md` about the advantages of splitting up the
code, especially in larger projects.

## Task 6

The CES function can be generalized to an arbitrary number of factors.

$$y =  a \cdot \left ( \sum_{j=1}^J \gamma_j x_j^{-\rho} \right )^{-\frac{1}{\rho}}$$

Implement a function called `general_ces` that takes a list of `factors`, a list of
`gammas`, `rho`, and `a` as arguments. The function should be in
`production_functions.py`. Also add a corresponding function evaluation and print
statements in `production_evaluations.py`

## Task 7

For this task you will implement functions in a new file called `tools.py` and call
those functions in `tool_evaluations.py`.

You will write Python functions to convert between two formats for storing tabular data
in pure-python data structures.

The first format is the **list of dicts**. Here, each list entry is a row of a table.
Let's look at an example:

```python
students_lod = [
    {"name": "Robin", "github_name": "ProgrammingGod42"},
    {"name": "Kim", "github_name": "CodingKim"},
    {"name": "Jesse", "github_name": "JavascriptJesse"},
]
```

The second format is a **dict of lists**. Here, each dict entry is a column of a table.
This is how it looks for the same example:

```python
students_dol = {
    "name": ["Robin", "Kim", "Jesse"],
    "github_name": ["ProgrammingGod42", "CodingKim", "JavascriptJesse"],
}
```

Write the functions `convert_lod_to_dol` and `convert_dol_to_lod` to convert between the
formats. Here are a few remarks:

- You can assume that you indeed have tabular data. I.e. each dict in the list of dicts
  has the same keys and each list in the dict of lists has the same length.
- You do not need to do any error handling. Just assume you got valid inputs.
- You cannot make any assumptions on the number or names of dictionary keys.
- The two functions need to be exact inverses of each other, i.e. back and forth
  transformation will return an exact copy of the inputs

Add function calls in `tool_evaluations.py` using the examples above. Also add print
statements that let me verify that your functions work.

## Task 8

You continue to work in `tools.py` and `tool_evaluations.py`.

In this task you will write a function that converts the tabular data from the previous
task into a string that represents a markdown table. Given either `students_lod` or
`students_dol` from the previous task, they should produce the following string

```markdown
| name | github_name|
|------|-----|
| Robin | ProgrammingGod42 |
| Kim | CodingKim |
| Jesse | JavascriptJesse |
```

which will be rendered to this table:

| name  | github_name      |
| ----- | ---------------- |
| Robin | ProgrammingGod42 |
| Kim   | CodingKim        |
| Jesse | JavascriptJesse  |

Here are a few things that might help you:

New lines in Python strings are represented as `\n` (without any spacing around it).

```python
print("a\nb")
```

```
a
b
```

You can use Python's built-in
[`isinstance` function](https://docs.python.org/3/library/functions.html#isinstance) to
find out which format you got

```python
my_dict = {"a": 1}
isinstance(my_dict, dict)
```

```
True
```

You can combine two strings into one using `+`

```python
"Hello" + " World"
```

```
'Hello World'
```

And here are a few remarks:

- The function should be called `create_markdown_table` and its only argument should be
  called data.
- The padding around the cells can deviate. Anything that produces a similar markdown
  table when rendered is acceptable
- You do not need to do any error handling. Just assume you got valid inputs.
- Remember that you wrote functions to easily convert between the two formats. You can
  and should use one of them to make your life easier
