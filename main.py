import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pathlib import Path
from pydantic import BaseModel

app = FastAPI(title="Wine Quality Predictor", version="1.0.0")

LABEL_MAP = {0: "low", 1: "medium", 2: "high"}
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.pkl"
FEATURE_NAMES = [
    "fixed_acidity",
    "volatile_acidity",
    "citric_acid",
    "residual_sugar",
    "chlorides",
    "free_sulfur_dioxide",
    "total_sulfur_dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol",
]

if not MODEL_PATH.exists():
    raise RuntimeError("Modèle introuvable. Lance d'abord train.py.")

artifact = joblib.load(MODEL_PATH)
if isinstance(artifact, dict) and "model" in artifact:
    model = artifact["model"]
    feature_names = artifact.get("feature_names", FEATURE_NAMES)
else:
    model = artifact
    feature_names = FEATURE_NAMES


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
    return {
        "status": "ok",
        "model": "wine-quality-rf",
        "artifact": str(MODEL_PATH.name),
    }


@app.post("/predict")
def predict(features: WineFeatures):
    try:
        payload = features.model_dump()
        data = pd.DataFrame([[payload[column] for column in feature_names]], columns=feature_names)

        pred = model.predict(data)[0]
        pred_label = LABEL_MAP[int(pred)]
        proba = model.predict_proba(data)[0]
        confidence = round(float(max(proba)), 4)

        return {
            "prediction": pred_label,
            "confidence": confidence,
            "classes": list(LABEL_MAP.values()),
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))