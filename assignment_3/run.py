from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"


if __name__ == "__main__":
    # ==================================================================================
    # Define inputs for the Monte Carlo simulation
    # ==================================================================================
    true_params = np.ones(6)
    y_sd = 1.5
    cov_type = "random"
    mean = np.zeros(len(true_params))
    meas_sds = np.linspace(0, 5, 10) # measurement error std
    n_repetitions = 200
    rng = np.random.default_rng(925408)
    n_obs = 2_000

    # ==================================================================================
    # Do the actual Monte Carlo simulation
    # ==================================================================================
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

    # ==================================================================================
    # Create the plot
    # ==================================================================================
    fig = px.line(
        data_frame=data,
        y="bias",
        x="meas_sd",
        color="name",
    )

    # ==================================================================================
    # Save data and plot
    # ==================================================================================
    BLD = Path("bld")
    if not BLD.exists():
        BLD.mkdir()
    data.to_pickle(BLD / "results.pkl")
    fig.write_image(BLD / "bias.png")
