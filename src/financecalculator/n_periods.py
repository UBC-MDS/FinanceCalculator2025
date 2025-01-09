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
