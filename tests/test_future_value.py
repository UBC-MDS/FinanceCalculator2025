import pandas as pd
import pytest
from financecalculator.future_value import future_value

# Test the function is working as expected
def test_future_value_valid_input():
    result = future_value(principal=1000, annual_rate=5, n_periods=12, contribution=100)
    assert isinstance(result, pd.DataFrame)
    assert result['Future Value'][0] == pytest.approx(2279.05, rel=1e-2)
    assert result['Principal'][0] == 1000
    assert result['Contributions'][0] == 1200
    assert result['Interest Earned'][0] == pytest.approx(79.05, rel=1e-2)

# Ensure a 0 contribution is valid
def test_future_value_zero_contribution():
    result = future_value(1000, 5, 12, 0)
    assert isinstance(result, pd.DataFrame)
    assert result['Future Value'][0] == pytest.approx(1051.16, rel=1e-2)
    assert result['Principal'][0] == 1000
    assert result['Contributions'][0] == 0
    assert result['Interest Earned'][0] == pytest.approx(51.16, rel=1e-2)

# Ensure a negative contribution is valid
def test_future_value_negative_contribution():
    result = future_value(1000, 5, 12, -100)
    assert isinstance(result, pd.DataFrame)
    assert result['Future Value'][0] == pytest.approx(-177.34, rel=1e-2)
    assert result['Principal'][0] == 1000
    assert result['Contributions'][0] == -1200
    assert result['Interest Earned'][0] == pytest.approx(22.66, rel=1e-2)

# Test negative principal: returns values as expected
def test_future_value_negative_contribution():
    result = future_value(-1000, 5, 12, 50)  
    assert isinstance(result, pd.DataFrame)
    assert result['Future Value'][0] == pytest.approx(-437.22, rel=1e-2)  
    assert result['Principal'][0] == -1000
    assert result['Contributions'][0] == 600
    assert result['Interest Earned'][0] == pytest.approx(-37.22, rel=1e-2) 

# Test with a high annual_rate
def test_future_value_high_annual_rate():
    result = future_value(1000, 100, 12, 100)
    assert isinstance(result, pd.DataFrame)
    assert result['Future Value'][0] == pytest.approx(4548.68, rel=1e-2)
    assert result['Principal'][0] == 1000
    assert result['Contributions'][0] == 1200
    assert result['Interest Earned'][0] == pytest.approx(2348.68, rel=1e-2)

# Test for a principal of 0 gives valid results
def test_future_value_zero_principal():
    result = future_value(0, 5, 12, 100)  # 5% annual interest, $100 monthly contribution, 12 months
    assert isinstance(result, pd.DataFrame)
    assert result['Future Value'][0] == pytest.approx(1227.89, rel=1e-2) 
    assert result['Principal'][0] == 0
    assert result['Contributions'][0] == 1200
    assert result['Interest Earned'][0] == pytest.approx(27.89, rel=1e-2) 

# Test for large number of periods
def test_future_value_large_number_of_periods():
    result = future_value(1000, 5, 120, 100)  
    assert isinstance(result, pd.DataFrame)
    assert result['Future Value'][0] == pytest.approx(17163.67, rel=1e-2)  
    assert result['Principal'][0] == 1000
    assert result['Contributions'][0] == 12000
    assert result['Interest Earned'][0] == pytest.approx(4175.67, rel=1e-2) 

# Test invalid n_periods (negative or 0): should raise ValueError
def test_future_value_invalid_periods():
    with pytest.raises(ValueError):
        future_value(1000, 5, 0)
    with pytest.raises(ValueError):
        future_value(1000, 5, -12)

# Test invalid principal type: should raise TypeError
def test_future_value_invalid_principal_type():
    with pytest.raises(TypeError):
        future_value("a", 5, 12)

# Test invalid annual_rate type: should raise TypeError
def test_future_value_invalid_annual_rate_type():
    with pytest.raises(TypeError):
        future_value(1000, "a", 12)

# Test invalid n_periods type: float or string input should raise TypeError
def test_future_value_invalid_n_periods_type():
    with pytest.raises(TypeError):
        future_value(1000, 5, "a")
    with pytest.raises(TypeError):
        future_value(1000, 5, 1.5)

# Test invalid contribution type: should raise TypeError
def test_future_value_invalid_contribution_type():
    with pytest.raises(TypeError):
        future_value(1000, 5, 12, "a")

# Test if the warning appears for zero annual_rate
def test_future_value_warning_zero_annual_rate():
    with pytest.warns(UserWarning, match="You entered an annual interest rate of 0"):
        future_value(1000, 0, 12)

# Test if the warning appears for negative annual_rate
def test_future_value_warning_negative_annual_rate():
    with pytest.warns(UserWarning, match="Warning: You entered a negative interest rate."):
        future_value(1000, -5, 12)

# Test if the warning appears for annual rate between 0 and 1 (likely entered as a decimal instead of percentage)
def test_future_value_warning_rate_between_0_and_1():
    with pytest.warns(UserWarning, match="Did you mean to enter it as a percentage"):
        future_value(1000, 0.05, 12)

 # Test if warning appears for n_periods < 6 months   
def test_future_value_warning_low_n_periods():
    with pytest.warns(UserWarning, match="The number of periods entered seems quite low"):
        future_value(1000, 5, 1)