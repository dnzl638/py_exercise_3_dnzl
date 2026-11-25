# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

import cmath
import math

def quadratic(a, b, c):
    discriminant = b ** 2 - (4 * a * c)
    if discriminant >= 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)

    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

    return x1, x2
