"""
Exercise 08 - Lists
Programming 100
Author: Royce J. Porter
"""


def main():

    assets = []

    firewall = {
        "hostname": "Firewall",
        "ip_address": "192.168.1.10",
        "operating_system": "Linux",
        "risk_score": 92
    }

    assets.append(firewall)

    print("\nRegistered Assets\n")

    for asset in assets:
        print(asset["hostname"])


if __name__ == "__main__":
    main()
