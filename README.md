# Projet MLOps - Wine Quality

Ce dépôt implémente un mini projet MLOps complet autour du dataset **Wine Quality Red**.

## Objectif

Le projet couvre les briques demandées dans l'exercice :

- entraînement d'un modèle `scikit-learn`
- exposition du modèle via une API `FastAPI`
- conteneurisation avec Docker
- automatisation avec GitHub Actions

## Dataset choisi

- **Nom** : Wine Quality Red
- **Source** : UCI Machine Learning Repository
- **URL** : `https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv`

## Structure du projet

```text
.
├── .github/workflows/
│   ├── develop-release.yml
│   └── feature-training.yml
├── Dockerfile
├── main.py
├── requirements.txt
├── train.py
└── README.md
```

## 1. Entraînement du modèle

Le script `train.py` :

- charge le dataset distant
- transforme la variable `quality` en 3 classes : `low`, `medium`, `high`
- sépare les données en train/test
- entraîne un `RandomForestClassifier`
- affiche les métriques `accuracy` et `F1-score`
- sauvegarde l'artefact dans `model.pkl`

### Lancer l'entraînement en local

```zsh
python -m pip install -r requirements.txt
python train.py
```

## 2. API de prédiction

L'API FastAPI expose :

- `GET /health`
- `POST /predict`

### Lancer l'API en local

```zsh
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Tester les endpoints

```zsh
curl http://127.0.0.1:8000/health
```

```zsh
curl -X POST http://127.0.0.1:8000/predict \
	-H "Content-Type: application/json" \
	-d '{
		"fixed_acidity": 7.4,
		"volatile_acidity": 0.70,
		"citric_acid": 0.00,
		"residual_sugar": 1.9,
		"chlorides": 0.076,
		"free_sulfur_dioxide": 11.0,
		"total_sulfur_dioxide": 34.0,
		"density": 0.9978,
		"pH": 3.51,
		"sulphates": 0.56,
		"alcohol": 9.4
	}'
```

## 3. Dockerisation

Le `Dockerfile` :

- installe les dépendances Python
- copie les fichiers du projet
- entraîne le modèle pendant le build
- démarre l'API avec `uvicorn`

### Build et exécution Docker

```zsh
docker build -t mlops-wine-quality .
docker run -p 8000:8000 mlops-wine-quality
```

## 4. Pipeline CI

### Push vers `feature/*`

Le workflow `.github/workflows/feature-training.yml` :

- installe les dépendances
- exécute `python train.py`
- publie `model.pkl` comme artefact GitHub Actions

### Push vers `develop`

Le workflow `.github/workflows/develop-release.yml` :

- installe les dépendances
- exécute `python train.py`
- build l'image Docker
- publie l'image vers **GitHub Container Registry (GHCR)**

Image publiée :

- `ghcr.io/jordy500/mlops-wine-quality:latest`
- `ghcr.io/jordy500/mlops-wine-quality:<commit-sha>`

## Dépôt Git

- **Repository** : `https://github.com/Jordy500/MLops`
## Stack utilisée

- Python
- pandas
- scikit-learn
- FastAPI
- Docker
- GitHub Actions
