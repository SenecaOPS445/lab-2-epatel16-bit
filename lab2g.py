#!/usr/bin/env python3

# Author: Ebrahim Patel
# Author ID: epatel16
# Date Created: 2025/01/20

import sys

# Check if an argument was provided
if len(sys.argv) == 2:
    # If an argument was provided, use it as the timer value
    timer = int(sys.argv[1])
else:
    # If no argument was provided, set the timer to 3
    timer = 3

# While loop to count down from the timer
while timer > 0:
    print(timer)  # Print the current value of timer
    timer -= 1  # Decrease the timer by 1 on each iteration

# Print "blast off!" once the timer reaches 0
print("blast off!")

