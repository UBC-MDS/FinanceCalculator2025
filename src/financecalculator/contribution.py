def calculate_contribution(principal, future_value, annual_rate, n_periods):
    """
    Calculates the contribution required to pay off a loan or reach a specified future value.

    Parameters
    ----------
    principal : float
        The initial loan amount or investment (present value).
    future_value : float
        The target future value (amount remaining after n_periods, usually 0 for loans).
    annual_rate : float
        Annual interest rate (as a percentage, e.g., 5 for 5%).
    n_periods : int
        Total number of periods (e.g., months or years).

    Returns
    -------
    float
        The payment amount per period required to reach the specified future value 
        or pay off the loan.
    """
    # annual_rate /= 100  # Convert to decimal
    # rate_per_period = annual_rate / 12  # Monthly rate
    # if rate_per_period == 0:  # Handle zero interest case
    #     return (principal - future_value) / n_periods
    # return (principal * rate_per_period) / (1 - (1 + rate_per_period) ** -n_periods)
