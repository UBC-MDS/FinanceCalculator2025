from financecalculator.present_value import present_value
import pytest
import pandas as pd

def test_inputs_are_numbers():
    # Test that all inputs are numbers
    invalid_inputs = [
        ["10000", 5, 10, 200],  # principal is a string
        [10000, "5", 10, 200],  # annual_rate is a string
        [10000, 5, "10", 200],  # n_periods is a string
        [10000, 5, 10, "200"],  # contribution is a string
        [[], 5, 10, 200],       # principal is a list
        [10000, [], 10, 200],   # annual_rate is a list
        [10000, 5, [], 200],    # n_periods is a list
        [10000, 5, 10, []],     # contribution is a list
        [{}, 5, 10, 200],       # principal is a dictionary
        [10000, {}, 10, 200],   # annual_rate is a dictionary
        [10000, 5, {}, 200],    # n_periods is a dictionary
        [10000, 5, 10, {}],     # contribution is a dictionary
        [None, 5, 10, 200],       # principal is a None
        [10000, None, 10, 200],   # annual_rate is a None
        [10000, 5, None, 200],    # n_periods is a None
        [10000, 5, 10, None],     # contribution is a None
        [True, 5, 10, 200],       # principal is a boolean
        [10000, True, 10, 200],   # annual_rate is a boolean
        [10000, 5, True, 200],    # n_periods is a boolean
        [10000, 5, 10, True],     # contribution is a boolean
    ]
    for inputs in invalid_inputs:
        with pytest.raises(ValueError, match="All input must be numbers"):
            present_value(*inputs)

def test_n_periods_positive_integer():
    # Test that n_periods is a non-zero positive integer
    with pytest.raises(ValueError, match="n_periods must be positive integer"):
        present_value(10000, 5, 0, 200)  # n_periods is zero
    with pytest.raises(ValueError, match="n_periods must be positive integer"):
        present_value(10000, 5, -5, 200)  # n_periods is negative
    with pytest.raises(ValueError, match="n_periods must be positive integer"):
        present_value(10000, 5, 5.5, 200)  # n_periods is not an integer

def test_overflow_and_underflow():
    # Test for overflow and underflow conditions
    large_principal = 1e20
    large_contribution = 1e20
    large_annual_rate = 1e5
    large_n_periods = 1e5
    result = present_value(large_principal, large_annual_rate, large_n_periods, large_contribution)
    assert result["Present Value"].iloc[0] < float('inf'), "Overflow error in present value calculation"

    small_annual_rate = 1e-10
    result = present_value(10000, small_annual_rate, 10, 200)
    assert result["Present Value"].iloc[0] > 0, "Underflow error in present value calculation"

def test_return_type():
    # Test that the return type is a DataFrame
    result = present_value(10000, 5, 10, 200)
    assert isinstance(result, pd.DataFrame), "Return type is not a DataFrame"