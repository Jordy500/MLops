from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="Wine Quality Predictor", version="1.0.0")

# Dictionnaire simple à la place du LabelEncoder
LABEL_MAP = {0: "low", 1: "medium", 2: "high"}

# Chargement du modèle au démarrage
MODEL_PATH = "model.pkl"

if not os.path.exists(MODEL_PATH):
    raise RuntimeError("Modèle introuvable. Lance d'abord train.py.")

model = joblib.load(MODEL_PATH)


# Schéma d'entrée
class WineFeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float


@app.get("/health")
def health():
    return {"status": "ok", "model": "wine-quality-rf"}


@app.post("/predict")
def predict(features: WineFeatures):
    try:
        data = np.array([[
            features.fixed_acidity,
            features.volatile_acidity,
            features.citric_acid,
            features.residual_sugar,
            features.chlorides,
            features.free_sulfur_dioxide,
            features.total_sulfur_dioxide,
            features.density,
            features.pH,
            features.sulphates,
            features.alcohol,
        ]])

        pred = model.predict(data)[0]
        pred_label = LABEL_MAP[int(pred)]
        proba = model.predict_proba(data)[0]
        confidence = round(float(np.max(proba)), 4)

        return {
            "prediction": pred_label,
            "confidence": confidence,
            "classes": list(LABEL_MAP.values())
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))