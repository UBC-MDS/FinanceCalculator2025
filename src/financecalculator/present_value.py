import pandas as pd
import warnings

def present_value(principal, annual_rate, n_periods, contribution=0):
    """
    Calculates the present value of an investment or loan, accounting for optional contributions.

    Parameters
    ----------
    principal : float
        The initial investment or loan amount.
    annual_rate : float
        Annual interest rate (as a percentage, e.g., 5 for 5%).
    n_periods : int
        Total number of periods (in months), a non-zero positive integer.
    contribution : float, optional
        Payment made per period (monthly contributions). Defaults to 0 if not provided.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the following columns:
            - 'Present Value': The present value of the investment or loan.
            - 'Principal': The initial investment or loan amount.
            - 'Contributions': Total amount contributed over the investment period.
            - 'Interest Saved': The amount of interest avoided by paying a lump sum today instead 
                of spreading payments over time.

    Examples
    --------
    >>> present_value(principal=1000, annual_rate=5, n_periods=120, contribution=100)
    """

    # Check if all inputs are numbers
    if not all(isinstance(arg, (int, float)) and not isinstance(arg, bool) for arg in [principal, annual_rate, n_periods, contribution]):
        raise TypeError("Please enter numbers.")
    
    # Check if n_periods is positive integer
    if not isinstance(n_periods, int) or n_periods <= 0:
        raise ValueError("n_periods must be positive integer")
    
    # If annual rate provided <= 0, issue a warning as it's an unusual situation.
    if annual_rate <= 0:
        warnings.warn("Warning: You entered an annual rate <= 0. It's a rare situation of a loss in value or no interest in loan.", UserWarning)

    # If annual rate is between 0 and 1, issue a warning as user may mistaken to input the rate as a decimal rather than percentage.
    if 0 < annual_rate <1:
        warnings.warn("Warning: Annual rate is percentage. E.g. if you want to enter 0.05 for 5%, please enter 5.", UserWarning)

    # If n_periods <=5, issue a warning as user may mistaken to input the years rather than months.
    if n_periods <= 5:
        warnings.warn("Warning: n period is by month. E.g. if you want to enter 1 year, please enter 12.", UserWarning)

    rate_per_period = annual_rate / (12 * 100) 

    if rate_per_period == 0:
        # Special case when interest rate is 0
        pv_contributions = contribution * n_periods
    else:
        # Calculate the present value of contributions (annuity formula)
        pv_contributions = contribution * ((1 - (1 + rate_per_period) ** -n_periods) / rate_per_period)

    # Total present value
    total_pv = pv_contributions + principal

    # Total contributions over the periods
    total_contributions = contribution * n_periods

    # Interest saved (difference between total contributions and present value)
    interest_saved = total_pv - total_contributions

    data = {
        "Present Value": [total_pv],
        "Principal": [principal],
        "Contributions": [total_contributions],
        "Interest Saved": [interest_saved],
    }

    return pd.DataFrame(data) 
