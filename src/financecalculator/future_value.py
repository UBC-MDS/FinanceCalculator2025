def future_value(principal, annual_rate, n_periods, contribution=0):
    """
    Calculates the future value of an investment with optional monthly contributions.

    Parameters
    ----------
    principal : float
        The initial investment.
    annual_rate : float
        Annual interest rate (as a percentage, e.g., 5 for 5%).
    n_periods : int
        Total number of periods (in months).
    contribution : float, optional
        Payment made per period (monthly contributions). Defaults to 0 if not provided.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the following columns:
            - 'Future Value': The future value of the investment, including contributions.
            - 'Principal': The initial investment.
            - 'Contributions': Total amount contributed over the investment period.
            - 'Interest Earned': The total interest earned from the investment.
    """