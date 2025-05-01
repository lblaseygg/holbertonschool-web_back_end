#!/usr/bin/env python3
"""
Async Comprehension module
Contains a coroutine that collects 10 random numbers using async comprehension
"""

from typing import List
from asyncio import gather

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator
    
    Returns:
        List of 10 random float values
    """
    return [num async for num in async_generator()]
