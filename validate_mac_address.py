"""
Author: Arun R Kaushik
Email: arunrkaushik@gmail.com
LinkedIn: https://www.linkedin.com/in/arunrkaushik/

Description: Python script to validate all sort of computer mac address
"""

import re

def is_valid_mac_address(mac_address):
    # Regular expression patterns to match MAC addresses
    mac_patterns = [
        r'^([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}$',
        r'^([0-9a-fA-F]{4}[:-]){2}[0-9a-fA-F]{4}$',
        r'^([0-9a-fA-F]{2}[.-]){5}[0-9a-fA-F]{2}$',
        r'^([0-9a-fA-F]{4}[.-]){2}[0-9a-fA-F]{4}$',
        r'^([0-9a-fA-F]{2}[--]){5}[0-9a-fA-F]{2}$',
        r'^([0-9a-fA-F]{4}[--]){2}[0-9a-fA-F]{4}$'
    ]
    
    # Check if the MAC address matches any of the patterns
    for pattern in mac_patterns:
        if re.match(pattern, mac_address):
            return True
    return False

# Test cases
test_addresses = [
    "12:34:56:78:9A:BC",
    "1234-5678-9ABC",
    "12.34.56.78.9A.BC",
    "1234.5678.9ABC",
    "12--34--56--78--9A",
    "1234--5678--9ABC",
    "InvalidMAC",
]

for address in test_addresses:
    if is_valid_mac_address(address):
        print(f"{address} is a valid MAC address.")
    else:
        print(f"{address} is NOT a valid MAC address.")
