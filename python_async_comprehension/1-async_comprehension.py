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
    over async_generator. It asynchronously iterates over the generator
    to collect exactly 10 random numbers between 0 and 10.
    """
    return [number async for number in async_generator()]
