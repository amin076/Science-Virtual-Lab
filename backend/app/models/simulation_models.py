"""
simulation_models.py — Pydantic models for simulation inputs/outputs.
"""

from pydantic import BaseModel, Field

class PendulumInput(BaseModel):
    theta0_deg: float = Field(10, ge=0, le=45, description="Initial angle in degrees (small-angle approx).")
    length_m: float = Field(1.0, gt=0, description="Pendulum length in meters.")
    g: float = Field(9.81, gt=0, description="Gravity in m/s^2.")
    t: float = Field(0.0, ge=0, description="Time in seconds.")

class PendulumResult(BaseModel):
    theta_rad: float
    theta_deg: float
    omega: float
