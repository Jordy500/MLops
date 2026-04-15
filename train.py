import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. Chargement du dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=";")

print(f"Dataset chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")

# 2. Prétraitement
# On transforme la qualité en 3 classes : low (<6), medium (6), high (>6)
def categorize(q):
    if q < 6:
        return "low"
    elif q == 6:
        return "medium"
    else:
        return "high"

df["quality_label"] = df["quality"].apply(categorize)

X = df.drop(columns=["quality", "quality_label"])
y = df["quality_label"]

le = LabelEncoder()
y_encoded = le.fit_transform(y)

# 3. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# 4. Entraînement
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Évaluation
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average="weighted")

print(f"Accuracy : {acc:.4f}")
print(f"F1-score : {f1:.4f}")

# 6. Sauvegarde du modèle et de l'encodeur
joblib.dump(model, "model.pkl")
joblib.dump(le, "label_encoder.pkl")

print("Modèle sauvegardé : model.pkl")
print("Encodeur sauvegardé : label_encoder.pkl")