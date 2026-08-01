"""
Exercise 06 - Loops
Programming 100
Author: Royce J. Porter
"""

print("=" * 50)
print(" Asset Inventory")
print("=" * 50)

assets = [
    "Firewall",
    "Web Server",
    "Domain Controller",
    "Database Server",
    "Workstation"
]

print("\nRegistered Assets\n")

for asset in assets:
    print(f"- {asset}")

print(f"\nTotal Assets: {len(assets)}")
