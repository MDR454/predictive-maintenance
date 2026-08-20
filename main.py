from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from src.features import compute_engine_features

app = FastAPI(title="Predictive Maintenance API")

ml_model = None

@app.on_event("startup")
def load_model():
    global ml_model
    try:
        ml_model = joblib.load("model.pkl")
    except Exception as e:
        ml_model = None

class SensorInput(BaseModel):
    air_temperature_k: float = Field(..., gt=200, lt=400)
    process_temperature_k: float = Field(..., gt=200, lt=400)
    rotational_speed_rpm: float = Field(..., gt=0, lt=5000)
    torque_nm: float = Field(..., gt=0, lt=300)
    tool_wear_min: float = Field(..., ge=0, lt=1000)

@app.get("/health")
def health_check():
    return {"status": "ok", "model_loaded": ml_model is not None}

@app.post("/predict")
def predict(data: SensorInput):
    if ml_model is None:
        raise HTTPException(status_code=500, detail="Модель не загружена")
    
    try:
        # Использование вынесенного модуля src.features
        derived = compute_engine_features(
            air_temp=data.air_temperature_k,
            process_temp=data.process_temperature_k,
            speed=data.rotational_speed_rpm,
            torque=data.torque_nm
        )
        
        df_row = pd.DataFrame([{
            'air_temperature_k': data.air_temperature_k,
            'process_temperature_k': data.process_temperature_k,
            'rotational_speed_rpm': data.rotational_speed_rpm,
            'torque_nm': data.torque_nm,
            'tool_wear_min': data.tool_wear_min,
            'temp_diff_k': derived['temp_diff_k'],
            'power': derived['power']
        }])
        
        prob = float(ml_model.predict_proba(df_row)[0][1])
        status = "HIGH_RISK" if prob > 0.24 else "NORMAL"
        
        return {
            "machine_status": status,
            "failure_probability": round(prob, 4)
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
