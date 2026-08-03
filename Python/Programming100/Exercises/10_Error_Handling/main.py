"""
Exercise 10 - Error Handling
Programming 100
Author: Royce J. Porter
"""


def get_port() -> int:
    """Collect and validate a TCP port number from the user."""

    while True:
        try:
            port = int(input("Enter a TCP port number: "))

            if port < 0 or port > 65535:
                raise ValueError("Port must be between 0 and 65535.")

            return port

        except ValueError as error:
            print(f"Invalid input: {error}")


def classify_port(port: int) -> str:
    """Classify a TCP port by range."""

    if port <= 1023:
        return "Well-Known Port"

    if port <= 49151:
        return "Registered Port"

    return "Dynamic or Private Port"


def main() -> None:
    """Run the error-handling exercise."""

    print("=" * 50)
    print(" Port Validation Utility")
    print("=" * 50)

    port = get_port()
    classification = classify_port(port)

    print(f"\nPort: {port}")
    print(f"Classification: {classification}")


if __name__ == "__main__":
    main()
