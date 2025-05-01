#!/usr/bin/env python3
"""
Measure Runtime module
Contains a coroutine that measures the runtime of executing async_comprehension
four times in parallel
"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime
    
    Returns:
        Total runtime in seconds (float)
    """
    start_time = time.perf_counter()
    
    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = time.perf_counter()
    
    return end_time - start_time
