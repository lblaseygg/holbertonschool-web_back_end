#!/usr/bin/env python3
"""
Module for pagination helper functions
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start index and end index for pagination.
    
    Args:
        page (int): The current page number (1-indexed)
        page_size (int): The number of items per page
        
    Returns:
        Tuple[int, int]: A tuple containing start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    return (start_index, end_index)
