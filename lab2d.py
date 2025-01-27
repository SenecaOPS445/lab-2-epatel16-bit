#!/usr/bin/env python3

import sys

# Check if exactly two additional arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)  # Exit with code 0 to indicate a successful termination

# Assign arguments to variables
name = sys.argv[1]
age = int(sys.argv[2])

# Output the result
print("Hi " + name + ", you are " + str(age) + " years old.")

