"""
Exercise 05 - Conditional Logic
Programming 100
Author: Royce J. Porter
"""

print("=" * 50)
print(" Port Classification Utility")
print("=" * 50)

port = int(input("Enter a TCP port number: "))

print()

if port < 0 or port > 65535:
    print("Invalid port number.")

elif port <= 1023:
    print(f"Port {port} is a Well-Known (Privileged) Port.")

elif port <= 49151:
    print(f"Port {port} is a Registered Port.")

else:
    print(f"Port {port} is a Dynamic / Private Port.")
