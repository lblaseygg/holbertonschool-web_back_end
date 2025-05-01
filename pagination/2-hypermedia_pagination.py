#!/usr/bin/env python3
"""
Module for hypermedia pagination implementation with a Server class
"""
import csv
import math
from typing import List, Tuple, Dict, Any


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset based on pagination parameters.
        
        Args:
            page (int): The page number (1-indexed)
            page_size (int): The number of items per page
            
        Returns:
            List[List]: A list of rows for the requested page
        """
        # Validate input parameters
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"
        
        # Get dataset
        dataset = self.dataset()
        
        # Calculate start and end indices
        start_index, end_index = index_range(page, page_size)
        
        # Return the appropriate page or empty list if out of range
        if start_index >= len(dataset):
            return []
        
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary with hypermedia pagination information.
        
        Args:
            page (int): The page number (1-indexed)
            page_size (int): The number of items per page
            
        Returns:
            Dict: A dictionary containing pagination metadata and data
        """
        # Get the page data
        data = self.get_page(page, page_size)
        
        # Calculate total items in dataset
        total_items = len(self.dataset())
        
        # Calculate total pages
        total_pages = math.ceil(total_items / page_size) if page_size > 0 else 0
        
        # Determine next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        
        # Create hypermedia dictionary
        hypermedia = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        
        return hypermedia
