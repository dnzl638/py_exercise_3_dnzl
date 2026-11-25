# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

def interest(capital, rate, years=1, tax=0):
    """Calculates the net compound interest earned over a given number of years."""

    if not (0 <= rate <= 1):
        raise ValueError("Rate must be between 0 and 1.")
    if not (0 <= tax <= 1):
        raise ValueError("Tax must be between 0 and 1.")
    if not isinstance(years, int) or years < 0:
        raise ValueError("Years must be a non-negative integer.")

    current_capital = capital
    for _ in range(years):
        yearly_interest = current_capital * rate
        if tax > 0:
            yearly_interest *= (1 - tax)
        current_capital += yearly_interest

    return current_capital - capital

def terminal_value(capital, rate, years=1, tax=0):
    """Calculates the final value of the investment after compound interest and taxes."""
    return capital + interest(capital, rate, years, tax)
