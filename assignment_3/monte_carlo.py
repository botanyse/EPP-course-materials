import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"


def do_monte_carlo(true_params, y_sd, cov_type, mean, meas_sds, n_repetitions,seed, n_obs):
    """Run a Monte Carlo simulation for a multivariate linear regrassion to study the impact of measurement error in the first independent variable.
    
    Args:
        true_params (float): The true coefficients vector of regression model
        y_sd (float): The standard deviation of the error term, i.e. of dependent variable y
        cov_type (str): The type of covariance-matrix of independent variables,
        either "random" or "deterministic"
        mean (float): The expected value of independent variables
        meas_sds (float): The standard deviation of measurement error
        n_repetitions (int): Number of repetitions in the simulation
        seed (int): A random number generator seed
        n_obs (int): Number of observations

    Returns: 
        data (DataFrame): Simulation result of Bias, Root-Mean-Sqaure Deviation (rmse), and Standard Deviation of Measurement Error(meas_sd) for each independent x variable.

    Raises:
        ValueError: If invalid cov_type input is given.

    """
    rng = np.random.default_rng(seed)
    n_params = len(true_params)
    # Set up parameter names for plotting
    names = [f"x_{i}" for i in range(len(true_params))]
    # Initialize list to which we will append DataFrames that are concatenated later
    to_concat = []
    for meas_sd in meas_sds:
        # Create a covariance matrix for the x variables
        if cov_type == "deterministic":
            cov = np.eye(n_params) + 0.2
        elif cov_type == "random":
            # Create a random but valid (i.e. symmetric positive semi-definite)
            # covariance matrix by multiplying a random matrix with its transpose
            # every matrix UU.T is positive semidefinite
            # and adding 1 to the diagonal to improve conditioning
            # because adding 1 to the diagonal ensures that our matrix is
            # always invertible
            helper = rng.uniform(low=-1, high=1, size=(n_params, n_params))
            cov = helper @ helper.T + np.eye(n_params)
        else:
            msg = f"Invalid cov_type: {cov_type}. Must be 'random' or 'deterministic.'"
            raise ValueError(
                msg,
            )

        # Set up a list to which we will append parameter estimates
        estimates = []
        for _ in range(n_repetitions):
            # Create independent variables
            x = rng.multivariate_normal(mean=mean, cov=cov, size=n_obs)
            # Draw error
            # loc=mean, scale=std
            epsilon = rng.normal(loc=0, scale=y_sd, size=n_obs)
            # Calculate y (before adding measurement error!)
            y = x @ true_params + epsilon
            # Draw measurement error
            meas_error = rng.normal(loc=0, scale=meas_sd, size=n_obs)
            # Add measurement error
            x[:, 0] += meas_error
            # Calculate parameter estimates
            params = LinearRegression().fit(x, y).coef_
            # append them to the list of estimates
            estimates.append(params)

        # Set up empty DataFrame and add results we need for plotting
        df = pd.DataFrame()
        deviations = np.array(estimates) - true_params
        df["name"] = names
        df["bias"] = deviations.mean(axis=0)
        df["rmse"] = np.sqrt((deviations**2).mean(axis=0))
        df["meas_sd"] = meas_sd
        to_concat.append(df)

    # Concatenate the DataFrame
    data = pd.concat(to_concat)
    return data