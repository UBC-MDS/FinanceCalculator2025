import pytest
import pandas as pd
from financecalculator.present_value import present_value

# Test error

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
        with pytest.raises(TypeError, match="Please enter numbers"):
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
    large_n_periods = int(1e5)
    result = present_value(large_principal, large_annual_rate, large_n_periods, large_contribution)
    assert result["Present Value"].iloc[0] < float('inf'), "Overflow error in present value calculation"

    small_annual_rate = 1e-10
    result = present_value(10000, small_annual_rate, 10, 200)
    assert result["Present Value"].iloc[0] > 0, "Underflow error in present value calculation"

def test_return_type():
    # Test that the return type is a DataFrame
    result = present_value(10000, 5, 10, 200)
    assert isinstance(result, pd.DataFrame), "Return type is not a DataFrame"

# Test edges

def test_zero_interest_rate():
    principal = 10000
    annual_rate = 0  # Zero interest rate
    n_periods = 12
    contribution = 500
    result = present_value(principal, annual_rate, n_periods, contribution)
    expected_present_value = principal + contribution * n_periods
    assert result["Present Value"].iloc[0] == expected_present_value

def test_no_contribution():
    principal = 10000
    annual_rate = 5
    n_periods = 12
    contribution = 0  # No contribution
    result = present_value(principal, annual_rate, n_periods, contribution)
    # No contribution, so present value is just the discounted principal
    assert result["Present Value"].iloc[0] > 0
    assert result["Contributions"].iloc[0] == 0

def test_negative_interest_rate():
    principal = 10000
    annual_rate = -5  # Negative interest rate
    n_periods = 12
    contribution = 500
    result = present_value(principal, annual_rate, n_periods, contribution)
    # Ensure the present value decreases due to negative interest rate
    assert result["Present Value"].iloc[0] > principal

def test_one_period():
    principal = 10000
    annual_rate = 5
    n_periods = 1  # Single period
    contribution = 500
    result = present_value(principal, annual_rate, n_periods, contribution)
    expected_present_value = principal + contribution / (1 + (annual_rate / 12 / 100))  # Discounted single contribution
    assert result["Present Value"].iloc[0] == pytest.approx(expected_present_value, rel=1e-9)

# Warnings

# Test if the warning appears for annual_rate <= 0
def test_annual_rate_below_zero():
    with pytest.warns(UserWarning, match="Warning: You entered an annual rate <= 0. It's a rare situation of a loss in value or no interest in loan."):
        present_value(1000, -3, 12)

# Test if the warning appears for annual rate between 0 and 1
def test_annual_rate_between_0_and_1():
    with pytest.warns(UserWarning, match="Warning: Annual rate is percentage. If you want to enter 0.05 for 5%, please enter 5."):
        present_value(1000, 0.9, 12)

 # Test if warning appears for n_periods < 6 months   
def test_low_n_periods():
    with pytest.warns(UserWarning, match="Warning: n period is by month. If you want to enter 1 year, please enter 12."):
        present_value(1000, 5, 3)
