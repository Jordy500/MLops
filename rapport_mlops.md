# Rapport Mini Projet MLOps - Wine Quality

**Date:** 15 avril 2026

---

## 📋 Informations du Projet

| Champ | Valeur |
|-------|--------|
| **Nom et Prénom** | Jordan NGUEKO |
| **Dataset choisi** | Wine Quality Red (UCI Machine Learning Repository) |
| **URL du dépôt Git** | https://github.com/Jordy500/MLops |
| **Branche par défaut** | main |
| **Branche développement** | develop |

---

## 🎯 Objectif du Projet

Réaliser un mini projet MLOps complet couvrant :
- ✅ Entraînement d'un modèle machine learning
- ✅ Exposition du modèle via une API REST
- ✅ Conteneurisation avec Docker
- ✅ Automatisation avec une pipeline CI

---

## 📊 Stack Technique

| Composant | Technologie |
|-----------|-------------|
| **Langage** | Python 3.11 |
| **ML Framework** | scikit-learn (RandomForest) |
| **API** | FastAPI + uvicorn |
| **Conteneurisation** | Docker |
| **CI/CD** | GitHub Actions |
| **Registre Docker** | GitHub Container Registry (GHCR) |

---

## 🚀 Livrables Complétés

### 1. **Entraînement du modèle** ✅

**Fichier:** `train.py`

**Fonctionnalités:**
- Charge le dataset Wine Quality Red depuis UCI ML Repository
- Transformation de la variable `quality` en 3 classes : `low`, `medium`, `high`
- Split train/test (80/20) avec stratification
- Entraînement d'un RandomForestClassifier (100 estimators)
- Évaluation avec Accuracy et F1-score

**Métriques obtenues:**
```
Dataset chargé : 1599 lignes, 12 colonnes
Accuracy : 0.7312
F1-score : 0.7300
Modèle sauvegardé : model.pkl
```

### 2. **API de Prédiction** ✅

**Fichier:** `main.py`

**Endpoints exposés:**

#### GET /health
```bash
curl http://localhost:8000/health
```
**Réponse:**
```json
{
  "status": "ok",
  "model": "wine-quality-rf",
  "artifact": "model.pkl"
}
```

#### POST /predict
```bash
curl -X POST http://localhost:8000/predict \
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
**Réponse:**
```json
{
  "prediction": "low",
  "confidence": 0.99,
  "classes": ["low", "medium", "high"]
}
```

### 3. **Dockerisation** ✅

**Fichier:** `Dockerfile`

**Caractéristiques:**
- Image de base : `python:3.11-slim`
- Installation des dépendances
- Copie du projet
- Entraînement du modèle lors du build
- Démarrage de l'API sur le port 8000

**Construction et exécution:**
```bash
docker build -t mlops-wine-quality .
docker run -p 8000:8000 mlops-wine-quality
```

**Image publiée:**
- `ghcr.io/jordy500/mlops-wine-quality:latest`
- `ghcr.io/jordy500/mlops-wine-quality:<commit-sha>`

### 4. **Pipeline CI** ✅

#### Workflow 1: Feature Training Pipeline
**Branch:** `feature/*`
**Fichier:** `.github/workflows/feature-training.yml`

**Étapes:**
1. Setup Python 3.11
2. Install dependencies
3. Train model (python train.py)
4. Upload model artifact

**Résultat:** ✅ **Completed successfully** (30 secondes)
**URL:** https://github.com/Jordy500/MLops/actions/runs/24456896136

---

#### Workflow 2: Develop Release Pipeline
**Branch:** `develop`
**Fichier:** `.github/workflows/develop-release.yml`

**Étapes:**
1. Setup Python 3.11
2. Install dependencies
3. Train model (python train.py)
4. Upload model artifact
5. Log in to GitHub Container Registry
6. Build and push Docker image to GHCR

**Résultat:** ✅ **Completed successfully** (1 minute 23 secondes)
**URL:** https://github.com/Jordy500/MLops/actions/runs/24456901847

---

## 📁 Structure du Projet

```
MLops/
├── .github/
│   └── workflows/
│       ├── feature-training.yml      # CI pour feature branches
│       └── develop-release.yml       # CI+CD pour develop
├── train.py                           # Script d'entraînement
├── main.py                            # API FastAPI
├── Dockerfile                         # Image Docker
├── .dockerignore                      # Optimisation build Docker
├── requirements.txt                   # Dépendances Python
├── README.md                          # Documentation
└── model.pkl                          # Artefact du modèle (généré)
```

---

## 🔗 Références et Ressources

| Ressource | URL |
|-----------|-----|
| **Dépôt GitHub** | https://github.com/Jordy500/MLops |
| **Dataset** | https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/ |
| **Feature Training Workflow** | https://github.com/Jordy500/MLops/actions/runs/24456896136 |
| **Develop Release Workflow** | https://github.com/Jordy500/MLops/actions/runs/24456901847 |
| **FastAPI Documentation** | https://fastapi.tiangolo.com/ |
| **Docker Documentation** | https://docs.docker.com/ |
| **GitHub Actions Documentation** | https://docs.github.com/en/actions |

---

## ✅ Checklist Complétude

- [x] Entraînement du modèle avec métriques
- [x] API avec endpoints `/health` et `/predict`
- [x] Dockerfile fonctionnel
- [x] Workflow pour feature branches
- [x] Workflow pour develop (training + Docker + GHCR)
- [x] Documentation complète (README)
- [x] Preuves des workflows CI réussis
- [x] Rapport PDF

---

## 🎓 Apprentissages et Bonnes Pratiques

### Points clés du projet :

1. **Reproductibilité** : Utilisation de `random_state=42` et stratification
2. **Robustesse** : Chemins absolus pour éviter les erreurs de localisation
3. **Cohérence** : Normalisation des noms de features entre train et predict
4. **Conteneurisation** : Image Docker optimisée avec `.dockerignore`
5. **CI/CD** : Workflows automatisés pour test et déploiement
6. **Documentation** : README complet avec exemples d'utilisation

---

## 📝 Conclusion

Ce projet démontre une implémentation complète d'une pipeline MLOps, du développement local jusqu'à la publication automatisée d'une image Docker via GitHub Actions. L'architecture est modulaire, testable et ready for production.

**Date de génération:** 15 avril 2026
