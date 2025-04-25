#!/usr/bin/env python3
"""
This module provides a function that returns a list of tuples containing
elements and their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements and their lengths.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing each
            sequence and its length
    """
    return [(i, len(i)) for i in lst]
