"""
Exercise 03 - Data Types
Programming 100
Author: Royce J. Porter
"""

# String
username = "Royce"

# Integer
age = 38

# Float
confidence_score = 98.75

# Boolean
is_veteran = True

# List
tools = ["Python", "Git", "Wireshark"]

# Tuple
ports = (22, 80, 443)

# Dictionary
device = {
    "hostname": "Shieldhound-Lab",
    "ip_address": "192.168.1.100",
    "status": "Online"
}

print("=== Python Data Types ===\n")

print(f"username = {username}")
print(f"Type: {type(username)}\n")

print(f"age = {age}")
print(f"Type: {type(age)}\n")

print(f"confidence_score = {confidence_score}")
print(f"Type: {type(confidence_score)}\n")

print(f"is_veteran = {is_veteran}")
print(f"Type: {type(is_veteran)}\n")

print(f"tools = {tools}")
print(f"Type: {type(tools)}\n")

print(f"ports = {ports}")
print(f"Type: {type(ports)}\n")

print(f"device = {device}")
print(f"Type: {type(device)}")
