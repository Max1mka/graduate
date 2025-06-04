import numpy as np

from typing import Iterator
from itertools import product

def generate_bit_vectors(n: int) -> Iterator[np.ndarray]:
    """Генератор всех битовых векторов длины n + 1 с последним элементом = 1"""
    """
    n = 2
    [0, 0, 1]
    [0, 1, 1]
    [1, 0, 1]
    [1, 1, 1]
    """
    for bits in product([0, 1], repeat=n):
        yield np.array([*bits, 1], dtype=np.int8)
