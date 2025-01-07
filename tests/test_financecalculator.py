import sys; sys.path.append('.')
import pytest

# PMT FUNCTION
from src.financecalculator.financecalculator import calculate_pmt

def test_calculate_pmt():
    # test 1: example usage
    result = calculate_pmt(20000, 0, 5, 12)
    assert round(result, 2) == 1712.15  # monthly payment
    
    # test 2: zero int rate
    result = calculate_pmt(10000, 0, 0, 10)
    assert result == 1000  # monthly payment

    # test 3: with fv
    result = calculate_pmt(10000, 1000, 3, 12)
    assert round(result, 2) == 846.94  # monthly payment
