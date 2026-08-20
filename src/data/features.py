"""
Модуль для генерации признаков (Feature Engineering) датчиков оборудования.
"""

def compute_engine_features(air_temp: float, process_temp: float, speed: float, torque: float) -> dict:
    """
    Вычисляет производные признаки из сырых показаний датчиков.
    """
    if air_temp <= 0 or process_temp <= 0:
        raise ValueError("Температура в Кельвинах не может быть отрицательной или нулевой.")
        
    if process_temp < air_temp:
        raise ValueError("Температура процесса не может быть ниже температуры воздуха.")
        
    temp_diff_k = process_temp - air_temp
    power = speed * torque
    
    return {
        "temp_diff_k": round(temp_diff_k, 2),
        "power": round(power, 2)
    }
