# read version from installed package
from importlib.metadata import version
__version__ = version("financecalculator")

# PMT FUNCTION
from .financecalculator import calculate_pmt
