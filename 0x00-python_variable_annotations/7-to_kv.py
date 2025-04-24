#!/usr/bin/env python3
"""Module with to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Type-annotated function that returns a tuple from arguments"""
    return (k, float(v ** 2))
