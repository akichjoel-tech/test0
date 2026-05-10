# Flask ultra minimal (test de deploiement)

Base de projet tres legere, mais organisee comme un gros projet.

## Installation (dev)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
```

## Configuration

1. Copier `.env.example` vers `.env` si necessaire.
2. Ajuster les variables (`PORT`, `SECRET_KEY`, etc.).

## Lancement local

```powershell
python app.py
```

Ou avec Flask CLI:

```powershell
flask run
```

## Endpoints

- `GET /` : page HTML simple de verification
- `GET /health` : endpoint de sante (`{"status": "ok"}`)

## Tests et qualite

```powershell
ruff check .
pytest -q
```

## Lancement type deploiement

### Gunicorn

```powershell
gunicorn wsgi:app --bind 0.0.0.0:5000
```

### Docker

```powershell
docker compose up --build
```

## Fichiers principaux

- `app.py` : application Flask et routes
- `config.py` : configuration centralisee via variables d'environnement
- `wsgi.py` : point d'entree WSGI pour deploiement
- `.env.example` : modele de variables d'environnement
- `.gitignore` : exclusions Git standards Python
- `tests/test_app.py` : tests HTTP minimaux
- `.github/workflows/ci.yml` : CI (lint + tests)
