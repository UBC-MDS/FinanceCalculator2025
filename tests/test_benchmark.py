import pytest
from financecalculator2025.present_value import present_value
from financecalculator2025.n_periods import n_periods
from financecalculator2025.future_value import future_value
from financecalculator2025.contribution import calculate_contribution

def test_benchmark_present_value(benchmark):
    benchmark(lambda: present_value(1000000, 5, 100))

def test_benchmark_n_periods(benchmark):
    benchmark(lambda: n_periods(1000000, 5, 50000))

def test_benchmark_future_value(benchmark):
    benchmark(lambda: future_value(1000000, 5, 100))

def test_benchmark_calculate_contribution(benchmark):
    benchmark(lambda: calculate_contribution(1000000, 50000, 5, 100))