# Explicit line continuation
print("We are going to " \
"learn " \
"Explicit " \
"line " \
"continuation")


# Implicit line continuation


# Carriage Return 
import time
import sys

# Example: Live progress update # without Carriage Return
print("Without Carriage Return: ")
for i in range(8):
    sys.stdout.write(f"Progress: {i*10}%")
    sys.stdout.flush()
    time.sleep(0.1)
print() # Move to next line after completion   
#print("\n")

# Example: Live progress update # with Carriage Return
print("With Carriage Return: ")
for i in range(11):
    # with Carriage Return
    sys.stdout.write(f"\rProgress: {i*10}%")
    sys.stdout.flush()
    time.sleep(0.1)
print() # Move to next line after completion   