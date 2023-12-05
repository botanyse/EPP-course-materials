import numpy as np
import pandas as pd
import pytest
from monte_carlo import do_monte_carlo

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

@pytest.fixture
def inputs():
    return {
    "true_params" : np.ones(6),
    "y_sd" : 1.5,
    "cov_type" : "random",
    "mean" : np.zeros(6),
    "meas_sds" : np.linspace(0, 5, 10),
    "n_repetitions" : 200,
    "seed" : 925408,
    "n_obs" : 2_000,
    }
def test_monte_carlo_x0_parameter_biased_towards_zero(inputs):
    data = do_monte_carlo(**inputs)
    x = data.loc[data["name"] == "x_0", ["bias"]]
    x = x.iloc[3:] # taking bias values where it converges to -1
    actual =x.reset_index(drop=True).values
    expected = -np.ones_like(actual)
    np.testing.assert_array_almost_equal(np.round(actual),np.round(expected))
