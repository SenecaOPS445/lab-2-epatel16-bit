#!/usr/bin/env python3

import sys

# Assign command-line arguments to variables
name = sys.argv[1]  # First argument is the name
age = int(sys.argv[2])  # Second argument is the age, converted to integer

# Print the exact output as required
print("Hi " + name + ", you are " + str(age) + " years old.")

