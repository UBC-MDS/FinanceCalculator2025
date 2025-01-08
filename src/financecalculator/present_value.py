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
        Total number of periods (in months).
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
                of spreading payments over time.(Can be negative in ininvestment)
    """