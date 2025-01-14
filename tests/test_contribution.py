from financecalculator.contribution import calculate_contribution
import pytest

import sys; sys.path.append('.')

def test_calculate_contribution():
    # Test 1: Basic usage with positive interest rate and no future value
    result = calculate_contribution(principal=20000, future_value=0, annual_rate=5, n_periods=12)
    assert round(result, 2) == -1712.15  # Monthly withdrawal to reduce principal to zero

    # Test 2: Zero interest rate, future value < principal
    result = calculate_contribution(principal=10000, future_value=0, annual_rate=0, n_periods=10)
    assert round(result, 2) == -1000.00  # Repayment with no interest

    # Test 3: Zero interest rate, future value > principal
    result = calculate_contribution(principal=5000, future_value=10000, annual_rate=0, n_periods=5)
    assert round(result, 2) == 1000.00  # Monthly deposit

    # Test 4: With a future value target
    result = calculate_contribution(principal=10000, future_value=1000, annual_rate=3, n_periods=12)
    assert round(result, 2) == -929.13  # Monthly withdrawal including target future value

    # Test 5: Negative interest rate with repayment
    result = calculate_contribution(principal=20000, future_value=0, annual_rate=-2, n_periods=12)
    assert round(result, 2) == -1648.67  # Monthly withdrawal with negative interest
