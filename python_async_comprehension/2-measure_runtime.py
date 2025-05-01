#!/usr/bin/env python3
"""
Module that measures the runtime of parallel async comprehensions.
This module provides a coroutine that measures the execution time of parallel async comprehensions.
"""
import asyncio
import time
from typing import float
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
