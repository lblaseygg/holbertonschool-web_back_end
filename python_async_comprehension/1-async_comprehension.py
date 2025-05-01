#!/usr/bin/env python3
"""
Module that demonstrates the use of async comprehensions to collect random numbers.
This module provides a coroutine that collects random numbers using async comprehension.
"""
from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator.

    Returns:
        List[float]: A list of 10 random numbers between 0 and 10.
    """
    return [i async for i in async_generator()]
 