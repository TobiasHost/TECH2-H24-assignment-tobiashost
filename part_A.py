"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

import math
from numpy import std

num_lst = [1, 2, 3, 4, 5]

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    total = 0
    count = 0
    for i in x:
        total += i
        count += 1

    mean = total/count

    total_squared_difference = 0

    for y in x:
        squared_difference = (y - mean) ** 2
        total_squared_difference += squared_difference
    variance = total_squared_difference / count

    standardDeviation = math.sqrt(variance)
    
    return standardDeviation




def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    total = sum(x)
    length = len(x)
    mean = total / length

    variance = sum((i - mean) ** 2 for i in x) / length

    standardDeviation = math.sqrt(variance)

    return standardDeviation

print(std_loops(num_lst))
print(std_builtin(num_lst))
print(std(num_lst))