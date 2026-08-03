"""
Exercise 11 - Modules
Programming 100
Author: Royce J. Porter
"""

from asset_utils import create_asset, display_asset


def main() -> None:
    """Run the modules exercise."""

    asset = create_asset(
        hostname="Firewall",
        ip_address="192.168.1.10",
        operating_system="Linux",
    )

    display_asset(asset)


if __name__ == "__main__":
    main()
