[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/GK4fjQ2A)
# Epp Bonn 2023 - Assignment 3

### Task 2

**Like**: 

- The code is well-structured and partitioned into clear sections with clear comments. It is easy to follow and understand.

- Variable names are descriptive and self-explanatory.

- It includes error handling for invalid `cov_type` input.


**Dislike**:

- Monte Carlo Simulation code is not put into a function, which makes it harder to reuse and test it.

- Plotting and simulation code should not be included in `if __name__ == "__main__"`. Instead of using global variables for inputs, we can pass these as arguments to simulation and plotting functions.

- We can include more error handling for invalid inputs for simulation.

