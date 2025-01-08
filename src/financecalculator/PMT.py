def calculate_pmt(pv, fv, i_rate, n_periods):
    """
    Calculates the periodic payment (PMT) required to pay off a loan or reach a future value.

    Parameters
    ----------
    pv : float
        Present Value (loan amount or principal).
    fv : float
        Future Value (amount left after N periods, usually 0 for loans).
    i_rate : float
        Annual Interest Rate (as a percentage, e.g., 5 for 5%).
    n_periods : int
        Number of periods (e.g., months, years).

    Returns
    -------
    float
        The payment amount per period required to reach the specified future value 
        or pay off the loan.
    """
    i_rate /= 100  # Convert to decimal
    rate_per_period = i_rate / 12  # Monthly rate
    if rate_per_period == 0:  # Handle zero interest case
        return (pv - fv) / n_periods
    return (pv * rate_per_period) / (1 - (1 + rate_per_period) ** -n_periods)
