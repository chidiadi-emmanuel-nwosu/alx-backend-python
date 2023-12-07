#!/usr/bin/env python3
"""7-to_kv.py"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string k and an int OR float v as arguments
       and returns a tuple
    """
    v = float(v) if isinstance(v, float) else int(v)
    return (k, v * v)
