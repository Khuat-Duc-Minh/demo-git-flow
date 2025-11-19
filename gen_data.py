"""gen_data.py
Generate a list of integers.
"""
from typing import List, Optional
import random


def generate_data(n: int = 100, min_v: int = 0, max_v: int = 1000, seed: Optional[int] = None) -> List[int]:
    """Generate a list of n integers in range [min_v, max_v].

    Args:
    n: number of integers to generate (n >= 0)
    min_v: minimum value (inclusive)
    max_v: maximum value (inclusive)
    seed: optional random seed for reproducibility

    Returns:
    List[int]: list of integers
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if min_v > max_v:
        raise ValueError("min_v must be <= max_v")

    if seed is not None:
        random.seed(seed)

    return [random.randint(min_v, max_v) for _ in range(n)]

if __name__ == "__main__":
    # quick manual demo
    sample = generate_data(20, 0, 50, seed=42)
    print(sample)