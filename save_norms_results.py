import os
from typing import List
from datetime import datetime

def save_norms_results(results: List[dict], filename: str = None) -> str:
    """
    Сохраняет результаты вычислений норм в файл внутри папки projector_norms.
    
    Параметры:
        results: Словарь с результатами {матрица: норма}
        filename: Имя файла (если None, будет сгенерировано автоматически)
    
    Возвращает:
        Путь к сохраненному файлу
    """
    # Создаем папку, если ее нет
    os.makedirs("projector_norms", exist_ok=True)
    
    # Генерируем имя файла с временной меткой, если не указано
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"norms_results_{timestamp}.txt"
    
    filepath = os.path.join("projector_norms", filename)
    
    # Формируем содержимое файла
    content = []
    content.append("Результаты вычисления норм проекторов")
    content.append(f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    content.append("-" * 50)

    min_norm = results[0]['norm']
    
    for result in results:
        content.append(f"Файл: {result['file'] :<15}")
        content.append(f"Норма: {result['norm']:.8f}")
        content.append(f"Время вычисления: {result['time']:.6f} секунд")
        content.append("-" * 50)

        min_norm = min(min_norm, result['norm'])

    content.append(f"Минимальная норма: {min_norm:.8f}")
    
    # Записываем в файл
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(content))
    
    return filepath
