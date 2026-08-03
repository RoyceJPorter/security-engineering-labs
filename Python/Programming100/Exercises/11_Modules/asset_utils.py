"""
Exercise 11 - Modules
Programming 100
Author: Royce J. Porter
"""


def create_asset(hostname: str, ip_address: str, operating_system: str) -> dict:
    """Create and return a cyber asset."""

    asset = {
        "hostname": hostname,
        "ip_address": ip_address,
        "operating_system": operating_system
    }

    return asset


def display_asset(asset: dict) -> None:
    """Display asset information."""

    print("\nCyber Asset")
    print("-" * 30)
    print(f"Hostname: {asset['hostname']}")
    print(f"IP Address: {asset['ip_address']}")
    print(f"Operating System: {asset['operating_system']}")
