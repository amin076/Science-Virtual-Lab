# Science Virtual Lab – System Architecture

## 🧠 Overview

Science Virtual Lab is a web-based platform that allows users to simulate real-world scientific experiments interactively. The MVP focuses on basic physics experiments such as the simple pendulum and free fall.

## 🧱 High-Level Architecture

    User (Browser)
         │
         ▼
    [ Next.js Frontend (Vercel) ]
         │  REST API Calls (HTTPS)
         ▼
    [ FastAPI Backend (Cloud Run) ]
         │
         ▼
    [ Firebase Firestore / Auth ]

## ⚙️ Components

### 1. Frontend

- Built with Next.js (App Router) and TypeScript
- Uses Material UI (MUI) for interface components
- Three.js for 3D visualization of experiments
- Communicates with backend through REST API calls

### 2. Backend

- Developed with FastAPI (Python)
- Performs scientific calculations using NumPy and SciPy
- Defines endpoints for simulation:
  - /health → system status
  - /sim/pendulum → pendulum motion calculations
  - /sim/freefall → free fall motion calculations

### 3. Database and Authentication

- Firebase Firestore stores user experiment results
- Firebase Authentication handles user login and registration (Email/Password)
- Schema (MVP):
  /users
  /uid
  name, email

        /runs
          /run_id
            uid, experiment_type, input_params, output_results, createdAt

### 4. Deployment

- Frontend: Vercel (automatic build from GitHub)
- Backend: Google Cloud Run (containerized FastAPI)
- Database/Auth: Firebase
- Environment Variables: stored securely in Vercel and GCP Secret Manager

## 🛡️ Security Overview

- All traffic over HTTPS
- CORS restricted to Vercel domain after MVP
- .env files excluded from version control
- Firebase manages authentication tokens securely

## 📊 Future Expansion

| Area              | Planned Upgrade                          |
| ----------------- | ---------------------------------------- |
| Simulation Engine | WebSocket for live simulation            |
| Database          | PostgreSQL for complex analytics         |
| AI Integration    | LangChain or OpenAI API for explanations |
| Roles             | Teacher/Student dashboards               |
| Testing           | Pytest, Vitest, and Playwright (e2e)     |

## 🧩 Summary

- Frontend (Next.js) handles visualization and interaction.
- Backend (FastAPI) handles physics computations and APIs.
- Firebase handles authentication and data storage.
- Deployment is serverless and scalable (Vercel + Cloud Run).

_Document version: 0.1 — last updated by Amin & Chatty team._
