"""
Exercise 12 - Cyber Asset Manager
Risk scoring module
Author: Royce J. Porter
"""


def calculate_risk(
    criticality: int,
    exposure: int,
    threat_level: int,
) -> int:
    """Calculate a simple weighted asset risk score."""

    score = (
        criticality * 0.40
        + exposure * 0.30
        + threat_level * 0.30
    )

    return round(score)
