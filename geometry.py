# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

import math

def perimeter_right_triangle(c1, c2):
    hypotenuse = math.sqrt(c1 ** 2 + c2 ** 2)
    return c1 + c2 + hypotenuse

def area_right_triangle(c1, c2):
    return 0.5 * c1 * c2

def perimeter_circle(r):
    return 2 * math.pi * r

def area_circle(r):
    return math.pi * (r ** 2)

def surface_sphere(r):
    return 4 * math.pi * (r ** 2)

def volume_sphere(r):
    return (4 / 3) * math.pi * (r ** 3)

def surface_cylinder(r, h):
    return 2 * math.pi * r * (r + h)

def volume_cylinder(r, h):
    return 2 * math.pi * (r ** 2) * h

def surface_cone(r, h):
    slant_height = math.sqrt(r ** 2 + h ** 2)
    return math.pi * r * (r + slant_height)

def volume_cone(r, h):
    return (1 / 3) * math.pi * (r ** 2) * h
