[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/78q9nXCM)
# EPP Bonn 2023 - Assignment 2

1. In the imperative way the DataFrame is changed in-place many times and variables of the same name changed their content. Describe why this is a problem, especially when working in a jupyter notebook.

    - This poses a problem since DataFrame and variables have many intermediate states with their final state names. It becomes difficult to track which version of DataFrame is being used at a particular cell in the notebook.
    It becomes difficult to debug as DataFrame evolves over time, and it's not straightforward to identify the source of an issue. In Jupyter Notebook, the code is executed in chunks, so it is critical to understand the state of the variables at different points. Also, because DataFrame is modified in-place, the state of the data depends on the order of the execution, another user can get different results which leads to potential reproducibility issues. Finally, Jupyter Notebooks are designed to be executed cell-wise, and cells should ideally be independent of each other. Modifying the DataFrame and variables in-place violates this principle and may lead to unexpected behaviour when running individual cells.

2. Read the code in the functional way. Does any of the functions have a side effect on its inputs?

    - Functional way of programming requires writing pure functions that are designed to be pure, that is they do not have any side effects on their inputs. No function in the code has a side effect on its inputs, when we look at the `raw` DataFrame we can see that the values and variables didn't change. Functional way of programming leaves the original DataFrame unchanged.

3. The functional way contains three functions. One of them could be called the main function and the others are helper functions. Which one is the main function and why?

    - `clean_data` function can be called function while others `_clean_agreement_scale` and `_clean_favorite_language` are helper functions. `clean_data` function serves a central point which directs to what comes next. It is defined before helper functions, call them and produces output. Helper functions are designed to be called by the main function and they perform specific tasks in contrast to the main function.