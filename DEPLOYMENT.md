# Deployment Guide

## GitHub Deployment

```bash
# Initialize repository
git init
git add .
git commit -m "Initial commit: E-Commerce Cloud Data Engineering Pipeline"

# Push to GitHub
git remote add origin https://github.com/<your-username>/Cloud-Data-Engineering.git
git branch -M main
git push -u origin main
```

**Important before pushing:**
- Ensure `.env` is listed in `.gitignore` (already configured)
- Use `.env.example` to share credential structure without exposing secrets
- Never commit real passwords or API keys

---

## Neon PostgreSQL (Already Deployed)

Your database is hosted on [Neon](https://neon.tech) — a serverless PostgreSQL platform.

- Connection is managed via `database/db_connection.py`
- Credentials are stored in `.env` (never committed to Git)
- SSL is enforced (`sslmode="require"`)

---

## Running on a New Machine

```bash
git clone https://github.com/<your-username>/Cloud-Data-Engineering.git
cd Cloud-Data-Engineering
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Fill in your Neon credentials in .env
python main.py
```

---

## Optional: Deploy Analytics API on Render

1. Create a `app.py` using FastAPI to expose analytics endpoints
2. Add a `Procfile`:
   ```
   web: uvicorn app:app --host 0.0.0.0 --port $PORT
   ```
3. Push to GitHub
4. Connect repo to [Render](https://render.com) → New Web Service
5. Set environment variables in Render dashboard (same as `.env`)

---

## Optional: Docker

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

```bash
docker build -t cloud-data-engineering .
docker run --env-file .env cloud-data-engineering
```
