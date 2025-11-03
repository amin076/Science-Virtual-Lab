# Science Virtual Lab – API Documentation

## Overview

This document describes the REST API endpoints for the Science Virtual Lab backend.  
The backend is powered by FastAPI and exposes endpoints for simulation and system health checks.  
All responses are in JSON format.

Base URL (development):
http://localhost:8000

Base URL (production - after deployment):
https://science-virtual-lab-api.run.app

---

## Health Check

Endpoint:
GET /health

Description:
Returns a simple response to verify the backend is running.

Response Example:
{
"status": "ok"
}

---

## Simulation Endpoints

Endpoint:
POST /sim/pendulum

Description:
Simulates a simple pendulum motion based on initial parameters.

Request Body:
{
"theta0_deg": 10,
"length_m": 1.0,
"g": 9.81,
"t": 2.0
}

Response Example:
{
"theta_rad": 0.12345,
"theta_deg": 7.069,
"omega": 3.132
}

Error Response Example:
{
"detail": "Invalid parameters"
}

---

Endpoint:
POST /sim/freefall

Description:
Simulates a free fall motion under gravity.

Request Body:
{
"v0": 0,
"t": 2,
"g": 9.81
}

Response Example:
{
"v": 19.62,
"y": 19.62
}

---

## Authentication (Firebase)

Authentication is handled by Firebase Auth on the frontend.  
Each request to protected endpoints (future versions) will include an Authorization header:

    Authorization: Bearer <Firebase_ID_Token>

The backend will verify this token via Firebase Admin SDK (planned for later phases).

---

## Notes

- All requests and responses use application/json content type.
- Validation is handled via Pydantic models.
- Errors follow the standard FastAPI error structure.

---

Document version: 0.1 — maintained by Amin & Chatty team.
