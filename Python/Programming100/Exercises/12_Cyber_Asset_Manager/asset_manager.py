"""
Exercise 12 - Cyber Asset Manager
Asset management module
Author: Royce J. Porter
"""

from risk import calculate_risk


def create_asset(
    hostname: str,
    ip_address: str,
    operating_system: str,
    criticality: int,
    exposure: int,
    threat_level: int,
) -> dict:
    """Create and return a cyber asset with a calculated risk score."""

    risk_score = calculate_risk(
        criticality=criticality,
        exposure=exposure,
        threat_level=threat_level,
    )

    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "operating_system": operating_system,
        "criticality": criticality,
        "exposure": exposure,
        "threat_level": threat_level,
        "risk_score": risk_score,
    }


def display_assets(assets: list[dict]) -> None:
    """Display all registered cyber assets."""

    if not assets:
        print("\nNo assets are currently registered.")
        return

    print("\nRegistered Cyber Assets")
    print("=" * 50)

    for index, asset in enumerate(assets, start=1):
        print(f"\nAsset {index}")
        print("-" * 30)
        print(f"Hostname: {asset['hostname']}")
        print(f"IP Address: {asset['ip_address']}")
        print(f"Operating System: {asset['operating_system']}")
        print(f"Criticality: {asset['criticality']}")
        print(f"Exposure: {asset['exposure']}")
        print(f"Threat Level: {asset['threat_level']}")
        print(f"Risk Score: {asset['risk_score']}/10")
