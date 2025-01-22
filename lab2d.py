#!/usr/bin/env python3

import sys

# Check if the number of arguments is exactly 3 (including the script name)
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(1)  # Exit with an error code

# Assign command-line arguments to variables
name = sys.argv[1]  # First argument is the name
age = int(sys.argv[2])  # Second argument is the age, converted to integer

# Print the exact output as required
print("Hi " + name + ", you are " + str(age) + " years old.")

