#!/usr/bin/env python3
"""Module with make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function that returns a function that
    multiplies a float by argument
    """
    def multiply(n: float) -> float:
        """
        Type-annotated function that returns product of its argument
        and calling function argument
        """
        return n * multiplier
    return multiply
