"""Summing the elements of a list using different loops"""

__author__ = "730766896"


def w_sum(vals: list[float]) -> float:
    """Adds up the elements (integers and floats) in while and returns sum"""
    i = 0
    sum: float = 0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Adds up the elements (integers and floats) in for and returns sum"""
    sum: float = 0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Adds up the elements (integers and floats) in for range and returns sum"""
    sum: float = 0
    for elem in range(0, len(vals), 1):
        sum += vals[elem]
    return sum
