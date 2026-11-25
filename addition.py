# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

def sum_to(num):
    assert num >= 0, "Input must be greater than or equal to 0"
    total = 0
    for i in range(1, num + 1):
        total += i
    return total
