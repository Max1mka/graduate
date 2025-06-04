from time import perf_counter
from norm_by_simplex import norm_by_simplex
from save_norms_results import save_norms_results
from to_max_volume_simplex import to_max_volume_simplex
from read_hadamard_matrices import read_hadamard_matrices

# Размерность
N = 31
# Порядок обрабатываемых матриц Адамара
ADAMARD_ORDER = N + 1

results = []
hadamard_matrices = read_hadamard_matrices(ADAMARD_ORDER)

for file, matrix in hadamard_matrices:
    start = perf_counter()

    max_volume_simplex = to_max_volume_simplex(matrix)
    norm = norm_by_simplex(max_volume_simplex)

    end = perf_counter()

    results.append(dict(file=file, norm=norm, time=end - start))

save_norms_results(results, f"norm_{N}")
