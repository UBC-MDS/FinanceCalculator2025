import sys; sys.path.append('.')
import pytest
import warnings
from financecalculator2025.n_periods import n_periods

def test_n_periods_positive_values():
    # situation with all positive
    assert n_periods(1000, 5, 2000, contribution=100) == 9

def test_principal_equal_to_future_value():
    # situation with principal = future_value, should return 0
    assert n_periods(1000, 5, 1000, contribution=100) == 0

def test_n_periods_negative_values():
    # situation with all negative
    with pytest.warns(UserWarning, match="The annual_rate is zero or negative. This is unusual behavior."):
        assert n_periods(-1000, -5, -2000, contribution=-100) == 11

def test_n_periods_zero_interest_rate():
    # situation with zero annual rate
    with pytest.warns(UserWarning, match="The annual_rate is zero or negative. This is unusual behavior."):
        assert n_periods(1000, 0, 2000, contribution=100) == 10

def test_n_periods_no_contribution():
    # situation with no contribution
    assert n_periods(1000, 5, 2000, contribution=0) == 167

def test_n_periods_zero_principal_and_contribution():
    # situation with no contribution and no principal
    with pytest.raises(ValueError):
        n_periods(0, 5, 2000)

def test_n_periods_zero_interest_and_zero_contribution():
    # situation with zero annual rate and no contribution
    with pytest.warns(UserWarning, match="The annual_rate is zero or negative. This is unusual behavior."):
        with pytest.raises(ValueError):
            n_periods(1000, 0, 2000, contribution=0)

# Test invalid principal type: should raise TypeError
def test_n_periods_type_error():
    with pytest.raises(TypeError):
        n_periods("1000", 5, 2000)

# Test invalid annual_rate type: should raise TypeError
def test_n_periods_invalid_annual_rate_type():
    with pytest.raises(TypeError):
        n_periods(1000, "a", 2000)

# Test invalid future_value: should raise TypeError
def test_n_periods_invalid_future_value_type():
    with pytest.raises(TypeError):
        n_periods(1000, 5, "2000")

# Test invalid contribution: should raise TypeError
def test_n_periods_invalid_contribution_type():
    with pytest.raises(TypeError):
        n_periods(1000, 5, 2000, "50")

# Test warning appears for annual_rate between 0 and 1:
def test_n_periods_low_interest_warning():
    with warnings.catch_warnings(record=True) as w:
        n_periods(1000, 0.5, 2000)
        assert len(w) == 1
        assert issubclass(w[-1].category, UserWarning)

# Test warning appears for n_periods < 6 months
def test_n_periods_low_periods_warning():
    with warnings.catch_warnings(record=True) as w:
        n_periods(1000, 5, 1500, contribution=100)
        assert len(w) == 1
        assert issubclass(w[-1].category, UserWarning)

# Test warning appears for negative annual_rate:
def test_n_periods_negative_interest_warning():
    with warnings.catch_warnings(record=True) as w:
        n_periods(1000, -5, 2000)
        assert len(w) >= 1
        assert issubclass(w[-1].category, UserWarning)