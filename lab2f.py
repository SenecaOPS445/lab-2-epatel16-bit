#!/usr/bin/env python3

# Author: Ebrahim Patel 
# Author ID: epatel16
# Date Created: 2025/01/20

import sys

# Check if a command-line argument is provided
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <start timer value>")
    sys.exit(1)  # Exit with an error if not exactly one argument is provided

# Assign the first command-line argument to timer, converting it to an integer
timer = int(sys.argv[1])

# While loop to count down from the timer
while timer > 0:
    print(timer)  # Print the current value of timer
    timer -= 1  # Decrease the timer by 1 on each iteration

# Print "blast off!" once the timer reaches 0
print("blast off!")

