
# PMT FUNCTION
def calculate_pmt(pv, fv, i_rate, n_periods):
    """
    Calculate the periodic payment (PMT).
    
    :param pv: Present Value (loan amount or principal)
    :param fv: Future Value (amount left after N periods, usually 0 for loans)
    :param i_rate: Annual Interest Rate (as a percentage, e.g., 5 for 5%)
    :param n_periods: Number of periods (e.g., months, years)
    :return: Payment amount per period
    """
    i_rate /= 100  # Convert to decimal
    rate_per_period = i_rate / 12  # Monthly rate
    if rate_per_period == 0:  # Handle zero interest case
        return (pv - fv) / n_periods
    return (pv * rate_per_period) / (1 - (1 + rate_per_period) ** -n_periods)
