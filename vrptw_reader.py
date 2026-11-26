# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

import math


def read_string_list(filename="r101"):
    """Reads a VRPTW data file and returns a list of strings (one per customer entry)."""
    if not filename.endswith(".txt"):
        filename += ".txt"

    entries = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            stripped = line.strip()
            # Keep only data lines that start with a customer number (digit)
            if stripped and stripped[0].isdigit():
                entries.append(line.rstrip("\n"))

    return entries


def get_demand(entries, cust_no):
    """Returns the demand of a given customer number as a float."""
    for entry in entries:
        parts = entry.split()
        if int(parts[0]) == cust_no:
            return float(parts[3])
    raise ValueError(f"Customer number {cust_no} not found.")


def calc_distance(entries, cust_no1, cust_no2):
    coords = {}
    for entry in entries:
        parts = entry.split()
        c_num = int(parts[0])
        if c_num in (cust_no1, cust_no2):
            coords[c_num] = (float(parts[1]), float(parts[2]))

    if cust_no1 not in coords or cust_no2 not in coords:
        raise ValueError("One or both customer numbers were not found.")

    x1, y1 = coords[cust_no1]
    x2, y2 = coords[cust_no2]
    return math.hypot(x2 - x1, y2 - y1)
