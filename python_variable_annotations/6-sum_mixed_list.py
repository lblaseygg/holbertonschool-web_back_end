#!/usr/bin/env python3
"""
This module provides a function to sum a list of mixed integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of mixed integers and floats

    Args:
        mxd_lst (List[Union[int, float]]): The list of mixed integers and floats to sum

    Returns:
        float: The sum of the list of mixed integers and floats
    """
    return float(sum(mxd_lst))
