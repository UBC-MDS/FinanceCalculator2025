import pytest
from financecalculator.contribution import calculate_contribution
import warnings

def test_calculate_contribution_basic_cases():
    """
    Test basic cases of calculate_contribution.
    """
    # Test 1: Positive interest rate, no future value
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

def test_calculate_contribution_unusual_warnings():
    """
    Test calculate_contribution for warnings on unusual inputs.
    """
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        calculate_contribution(principal=1000, future_value=1000, annual_rate=0.5, n_periods=10)
        assert any("Annual interest rate is unusually low" in str(warning.message) for warning in w)
        
        calculate_contribution(principal=1000, future_value=1000, annual_rate=-1, n_periods=10)
        assert any("Annual interest rate is zero or negative" in str(warning.message) for warning in w)

        calculate_contribution(principal=1000, future_value=1000, annual_rate=5, n_periods=3)
        assert any("Number of periods is unusually low" in str(warning.message) for warning in w)

def test_calculate_contribution_edge_cases():
    """
    Test calculate_contribution for edge cases.
    """
    # Test 1: Single period
    result = calculate_contribution(principal=0, future_value=1000, annual_rate=0, n_periods=1)
    assert result == 1000.00

    # Test 2: High future value and zero principal
    result = calculate_contribution(principal=0, future_value=1000000, annual_rate=5, n_periods=120)
    assert round(result, 2) == 6439.88

    # Test 3: Large principal with zero future value
    result = calculate_contribution(principal=1000000, future_value=0, annual_rate=3, n_periods=240)
    assert round(result, 2) == -5545.98