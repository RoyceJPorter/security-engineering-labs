"""
Exercise 04 - User Input
Programming 100
Author: Royce J. Porter
"""

print("=== Security Asset Information ===\n")

hostname = input("Enter hostname: ")
ip_address = input("Enter IP address: ")
operating_system = input("Enter operating system: ")
port = input("Enter primary service port: ")

print("\n----- Asset Summary -----")
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print(f"Operating System: {operating_system}")
print(f"Primary Port: {port}")
