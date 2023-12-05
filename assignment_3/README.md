# Epp Bonn 2023 - Assignment 3

### Task 2

**Like**: 

- The code is well-structured and partitioned into clear sections with clear comments. It is easy to follow and understand.

- Variable names are descriptive and self-explanatory.

- It includes error handling for invalid `cov_type` input.


**Dislike**:

- Monte Carlo Simulation code is not put into a function, which makes it harder to reuse and test.

- Simulation code should not be included in `if __name__ == "__main__"`. Instead of using global variables for inputs, we can pass these as arguments to simulation function.

- We can include more error handling for invalid inputs for simulation.

