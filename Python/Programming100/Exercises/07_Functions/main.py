"""
Exercise 07 - Functions
Programming 100
Author: Royce J. Porter
"""


def display_banner():
    """Display the program title."""
    print("=" * 50)
    print(" Security Risk Calculator")
    print("=" * 50)


def calculate_risk(
    threat_score: float,
    asset_criticality: float,
    exposure_level: float,
) -> float:
    """
    Calculate a preliminary weighted risk score.

    Inputs are expected to be between 0.0 and 1.0.
    """

    weighted_score = (
        threat_score * 0.50
        + asset_criticality * 0.30
        + exposure_level * 0.20
    )

    return round(weighted_score * 100, 2)


def display_result(score: float):
    """Display the final risk score."""
    print(f"\nPreliminary Risk Score: {score}/100")


def main():
    """Run the program."""
    display_banner()

    risk_score = calculate_risk(
        threat_score=0.80,
        asset_criticality=0.90,
        exposure_level=0.70,
    )

    display_result(risk_score)


if __name__ == "__main__":
    main()
