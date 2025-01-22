#!/usr/bin/env python3

# Author: Ebrahim Patel 
# Author ID: epatel16
# Date Created: 2025/01/20

import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <start timer value>")
    sys.exit(1)  

timer = int(sys.argv[1])

while timer > 0:
    print(timer)  
    timer -= 1  

print("blast off!")

