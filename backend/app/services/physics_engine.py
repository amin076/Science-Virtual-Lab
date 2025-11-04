"""
physics_engine.py — core physics simulation logic for Science Virtual Lab.
Contains mathematical functions for scientific experiments (MVP: pendulum).
"""

import math
from app.models.simulation_models import PendulumInput, PendulumResult

def simulate_pendulum(data: PendulumInput) -> PendulumResult:
    """
    Simulate a simple pendulum using small-angle approximation.

    Equation of motion:
        θ(t) = θ₀ * cos(√(g/L) * t)

    Args:
        data (PendulumInput): input parameters for simulation

    Returns:
        PendulumResult: simulated results (θ in radians/degrees, ω)
    """
    theta0 = math.radians(data.theta0_deg)
    omega = math.sqrt(data.g / data.length_m)
    theta_t = theta0 * math.cos(omega * data.t)

    return PendulumResult(
        theta_rad=theta_t,
        theta_deg=math.degrees(theta_t),
        omega=omega
    )
