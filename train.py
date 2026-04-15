from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

DATASET_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.pkl"


def categorize_quality(quality_value: int) -> int:
    if quality_value < 6:
        return 0
    if quality_value == 6:
        return 1
    return 2


def load_dataset() -> pd.DataFrame:
    dataframe = pd.read_csv(DATASET_URL, sep=";")
    dataframe = dataframe.rename(columns=lambda column: column.strip().replace(" ", "_"))
    print(f"Dataset chargé : {dataframe.shape[0]} lignes, {dataframe.shape[1]} colonnes")
    return dataframe


def train_model() -> None:
    dataframe = load_dataset()
    dataframe["quality_label"] = dataframe["quality"].apply(categorize_quality)

    features = dataframe.drop(columns=["quality", "quality_label"])
    target = dataframe["quality_label"]
    feature_names = list(features.columns)

    X_train, X_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=42,
        stratify=target,
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions, average="weighted")

    print(f"Accuracy : {accuracy:.4f}")
    print(f"F1-score : {f1:.4f}")

    artifact = {
        "model": model,
        "feature_names": feature_names,
        "metrics": {
            "accuracy": accuracy,
            "f1_score": f1,
        },
    }
    joblib.dump(artifact, MODEL_PATH)

    print(f"Modèle sauvegardé : {MODEL_PATH}")


if __name__ == "__main__":
    train_model()