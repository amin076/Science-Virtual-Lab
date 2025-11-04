"""
simulations.py — API endpoints for scientific simulations.
Currently supports pendulum simulation.
"""

from fastapi import APIRouter, HTTPException
from app.models.simulation_models import PendulumInput, PendulumResult
from app.services.physics_engine import simulate_pendulum

router = APIRouter()

@router.post("/pendulum", response_model=PendulumResult)
def run_pendulum_simulation(data: PendulumInput):
    """
    Simulate a simple pendulum motion.

    Input:
        - theta0_deg: initial angle in degrees (0–45)
        - length_m: pendulum length in meters (>0)
        - g: gravity constant (default 9.81)
        - t: time in seconds

    Returns:
        PendulumResult: calculated theta and angular velocity.
    """
    try:
        result = simulate_pendulum(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
