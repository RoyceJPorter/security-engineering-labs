"""
Exercise 12 - Cyber Asset Manager
Programming 100 Capstone
Author: Royce J. Porter
"""

from asset_manager import create_asset, display_assets
from file_manager import load_assets, save_assets


def get_score(prompt: str) -> int:
    """Collect and validate a score between 1 and 10."""

    while True:
        try:
            score = int(input(prompt))

            if 1 <= score <= 10:
                return score

            print("Enter a value between 1 and 10.")

        except ValueError:
            print("Enter a whole number.")


def register_asset() -> dict:
    """Collect user input and create a cyber asset."""

    print("\nRegister Cyber Asset")
    print("=" * 50)

    hostname = input("Hostname: ").strip()
    ip_address = input("IP Address: ").strip()
    operating_system = input("Operating System: ").strip()

    criticality = get_score("Criticality (1-10): ")
    exposure = get_score("Exposure (1-10): ")
    threat_level = get_score("Threat Level (1-10): ")

    return create_asset(
        hostname=hostname,
        ip_address=ip_address,
        operating_system=operating_system,
        criticality=criticality,
        exposure=exposure,
        threat_level=threat_level,
    )


def display_menu() -> None:
    """Display the application menu."""

    print("\nCyber Asset Manager")
    print("=" * 50)
    print("1. Register Asset")
    print("2. Display Assets")
    print("3. Save Assets")
    print("4. Exit")


def main() -> None:
    """Run the Cyber Asset Manager application."""

    assets = load_assets()

    while True:
        display_menu()
        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            asset = register_asset()
            assets.append(asset)
            print("\nAsset registered successfully.")

        elif choice == "2":
            display_assets(assets)

        elif choice == "3":
            save_assets(assets)

        elif choice == "4":
            save_assets(assets)
            print("\nExiting Cyber Asset Manager.")
            break

        else:
            print("\nInvalid selection. Choose an option from 1 to 4.")


if __name__ == "__main__":
    main()
