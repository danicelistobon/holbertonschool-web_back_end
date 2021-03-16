#!/usr/bin/env python3
"""Takes a float multiplier as argument and returns a function that
    multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier
    """
    def mult(n: float) -> float:
        """Function
        """
        return float(n * multiplier)
    return mult
