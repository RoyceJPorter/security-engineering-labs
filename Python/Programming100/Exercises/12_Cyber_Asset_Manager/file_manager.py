"""
Exercise 12 - Cyber Asset Manager
File management module
Author: Royce J. Porter
"""

import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("assets.json")


def save_assets(assets: list[dict]) -> None:
    """Save registered assets to a JSON file."""

    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(assets, file, indent=4)

        print(f"\nSaved {len(assets)} asset(s) successfully.")

    except OSError as error:
        print(f"\nUnable to save assets: {error}")


def load_assets() -> list[dict]:
    """Load registered assets from a JSON file."""

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            assets = json.load(file)

        if isinstance(assets, list):
            return assets

        print("\nInvalid asset data format. Starting with an empty inventory.")
        return []

    except (OSError, json.JSONDecodeError) as error:
        print(f"\nUnable to load assets: {error}")
        return []
