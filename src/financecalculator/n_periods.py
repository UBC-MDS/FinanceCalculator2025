import math

def n_periods(principal, annual_rate, future_value, contribution=0):
    """
    Calculates the number of periods (in months) needed to reach a specified future value,
    given an initial principal, an annual interest rate, and optional monthly contributions.

    Parameters
    ----------
    principal : float
        The initial investment amount.
    annual_rate : float
        Annual interest rate (as a percentage, e.g., 5 for 5%).
    future_value : float
        The target future value of the investment.
    contribution : float, optional
        Payment made per period (monthly contributions). Defaults to 0 if not provided.

    Returns
    -------
    n_periods : int
        The number of periods (in months) required to reach the future value.
    """
    if principal == future_value:
        return 0
        
    # convert annual rate to monthly rate
    monthly_rate = annual_rate / 100 / 12

    # error raised when both principal and contribution are 0
    if principal == 0 and contribution == 0:
        raise ValueError("Either principal or contribution must be non-zero to reach a future value.")

    # if monthly rate is 0, just simple calculation 
    if monthly_rate == 0:
        if contribution == 0:
            raise ValueError("With a zero interest rate and no contribution, the future value cannot be reached.")
        n_periods = (future_value - principal) / contribution
    else:
    # compounding calculation
        n_periods = math.log((future_value * monthly_rate + contribution) / (principal * monthly_rate + contribution)) / math.log(1 + monthly_rate)

    # return a positive integar
    return max(1, round(n_periods))
    
