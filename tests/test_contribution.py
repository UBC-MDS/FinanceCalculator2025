import pytest
from financecalculator2025.contribution import calculate_contribution

def test_calculate_contribution_basic_cases():
    """
    Test basic cases of calculate_contribution.
    """
    # Test 1: Positive interest rate, no future value
    result = calculate_contribution(principal=20000, future_value=0, annual_rate=5, n_periods=12)
    assert round(result, 2) == -1712.15

    # Test 2: Zero interest rate, future value < principal
    result = calculate_contribution(principal=10000, future_value=0, annual_rate=0, n_periods=10)
    assert round(result, 2) == -1000.00

    # Test 3: Zero interest rate, future value > principal
    result = calculate_contribution(principal=5000, future_value=10000, annual_rate=0, n_periods=5)
    assert round(result, 2) == 1000.00

    # Test 4: With a future value target
    result = calculate_contribution(principal=10000, future_value=1000, annual_rate=3, n_periods=12)
    assert round(result, 2) == -929.13

    # Test 5: Negative interest rate with repayment
    with pytest.warns(UserWarning, match="Annual interest rate is zero or negative, which is uncommon"):
        result = calculate_contribution(principal=20000, future_value=0, annual_rate=-2, n_periods=12)
        assert round(result, 2) == -1648.67

    # Test 6: Unusually low number of periods
    with pytest.warns(UserWarning, match="Number of periods is unusually low"):
        result = calculate_contribution(principal=10000, future_value=1000, annual_rate=3, n_periods=1)
        print(f"Debug result: {result}")  # 调试信息
        assert round(result, 2) == -11025.00  # 更新预期值


def test_calculate_contribution_unusual_warnings():
    """
    Test calculate_contribution for warnings on unusual inputs using pytest.warns().
    """
    with pytest.warns(UserWarning, match="Annual interest rate is unusually low"):
        calculate_contribution(principal=1000, future_value=1000, annual_rate=0.5, n_periods=10)
    
    with pytest.warns(UserWarning, match="Annual interest rate is zero or negative"):
        calculate_contribution(principal=1000, future_value=1000, annual_rate=-1, n_periods=10)
    
    with pytest.warns(UserWarning, match="Number of periods is unusually low"):
        calculate_contribution(principal=1000, future_value=1000, annual_rate=5, n_periods=3)


def test_calculate_contribution_edge_cases():
    """
    Test calculate_contribution for edge cases.
    """
    # Test 1: Single period
    with pytest.warns(UserWarning, match="Number of periods is unusually low"):
        result = calculate_contribution(principal=0, future_value=1000, annual_rate=0, n_periods=1)
        assert result == 1000.00

    # Test 2: High future value and zero principal
    result = calculate_contribution(principal=0, future_value=1000000, annual_rate=5, n_periods=120)
    assert round(result, 2) == 6439.88

    # Test 3: Large principal with zero future value
    result = calculate_contribution(principal=1000000, future_value=0, annual_rate=3, n_periods=240)
    assert round(result, 2) == -5545.98


def test_input_validation():
    """
    Test calculate_contribution for incorrect input types.
    """
    with pytest.raises(ValueError, match="Principal must be a number."):
        calculate_contribution(principal="abc", future_value=1000, annual_rate=5, n_periods=12)

    with pytest.raises(ValueError, match="Future value must be a number."):
        calculate_contribution(principal=1000, future_value="abc", annual_rate=5, n_periods=12)

    with pytest.raises(ValueError, match="Annual rate must be a number and greater than or equal to -100%."):
        calculate_contribution(principal=1000, future_value=1000, annual_rate="five", n_periods=12)

    with pytest.raises(ValueError, match="Number of periods must be a positive integer."):
        calculate_contribution(principal=1000, future_value=1000, annual_rate=5, n_periods="abc")