import numpy as np

from generate_bit_vectors import generate_bit_vectors

def norm_by_simplex(sim: np.ndarray) -> float:
    """
    Вычисляет норму проектора для заданной симплексной матрицы.
    
    Параметры:
        sim: Симплексная матрица размера (N+1) x (N+1)
    
    Возвращает:
        Найденную норму проектора
    """
    N = sim.shape[0] - 1
    L: np.ndarray = np.linalg.inv(sim)
    max_norm: float = 0.0
    
    for x in generate_bit_vectors(N):
        lamb: np.ndarray = x @ L
        current_norm: float = np.sum(np.abs(lamb))
        max_norm = max(max_norm, current_norm)
    
    return max_norm