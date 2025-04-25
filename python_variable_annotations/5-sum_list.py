#!/usr/bin/env python3
"""
This module provides a function to sum a list of floating point numbers.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of floating point numbers

    Args:
        input_list (List[float]): The list of floating point numbers to sum

    Returns:
        float: The sum of the list of floating point numbers
    """
    return sum(input_list)
