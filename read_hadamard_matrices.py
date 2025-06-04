import os
import numpy as np

from pathlib import Path
from typing import List, Union, Tuple  

def convert_symbols_to_matrix(data: str) -> np.ndarray:
    """Преобразует строки с символами + и - в матрицу NumPy."""
    lines = [line.strip() for line in data.split('\n') if line.strip()]
    matrix = []

    for line in lines:
        row = []
        for char in line:
            if char == '+':
                row.append(1)
            elif char == '-':
                row.append(-1)
        matrix.append(row)

    return np.array(matrix)

def process_file(input_file: Union[str, Path]) -> np.ndarray:
    """Обрабатывает один файл: читает, преобразует и возвращает."""
    try:
        file_name = Path(input_file).name

        with open(input_file, 'r') as f:
            data = f.read()
        
        hadamard_matrix = convert_symbols_to_matrix(data)

        print(f"Файл '{file_name}' обработан'")
        
        return hadamard_matrix
        
    except Exception as e:
        print(f"Ошибка при обработке '{input_file}': {e}")

def read_hadamard_matrices(order: int) -> Tuple[Union[str, Path], List[np.ndarray]]:
    """Возвращает список матриц из всех файлов в папке"""
    matrices = []
    input_dir = f"hadamard_{order}"

    if not os.path.exists(input_dir):
        print(f"Папка '{input_dir}' не найдена!")
        return
    
    # Получаем список файлов (игнорируем подпапки)
    files = [
        os.path.join(input_dir, f) 
        for f in os.listdir(input_dir) 
        if os.path.isfile(os.path.join(input_dir, f))
    ]
    
    if not files:
        print(f"В папке '{input_dir}' нет файлов для обработки!")
        return
    
    print(f"Найдено {len(files)} файлов в '{input_dir}'")
    
    
    for file in files:
            matrices.append([file, process_file(file)])
    
    print("Все файлы успешно обработаны!")

    return matrices
