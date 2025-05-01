#!/usr/bin/env python3
"""
Module that defines an asynchronous generator for generating random numbers.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that loops 10 times, each time asynchronously waiting 1 second,
    then yielding a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10) 
