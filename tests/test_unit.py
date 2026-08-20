import pytest
from src.features import compute_engine_features

# === UNIT TESTS ===

def test_compute_engine_features_valid():
    """Проверка правильности расчетов при корректных входящих данных."""
    res = compute_engine_features(
        air_temp=298.0, 
        process_temp=308.0, 
        speed=1500.0, 
        torque=40.0
    )
    assert res["temp_diff_k"] == 10.0
    assert res["power"] == 60000.0

def test_compute_engine_features_invalid_temp_difference():
    """Проверка выброса исключения, если температура процесса ниже температуры воздуха."""
    with pytest.raises(ValueError) as exc_info:
        compute_engine_features(air_temp=310.0, process_temp=290.0, speed=1000.0, torque=20.0)
    assert "не может быть ниже" in str(exc_info.value)

def test_compute_engine_features_negative_temp():
    """Проверка реакции на отрицательную температуру."""
    with pytest.raises(ValueError):
        compute_engine_features(air_temp=-10.0, process_temp=300.0, speed=1000.0, torque=20.0)
