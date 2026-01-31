#Sorted Search with Conditions
from random import random
#1. Generate random data (Starter code)
# Create a list of 20 random values between 0 and 1
values = [random() for i in range(20)]
# Create a random value x to compare
x = random()
#2. Sort the list (the .sort() method sorts the list in place)
values.sort()
# Print sorted list and x (as required by the assignment)
print(f"Sorted Values: {values}")
print(f"Search Value (x): {x}")
#3. Find the first index where value >= x
found = False  #Flag variable to check if a match is found
for index, value in enumerate(values):
    #Check if the current value is greater than or equal to x
    if value >= x:
        print(f"First matching index is: {index}")
        print(f"Value at that index: {value}")
        found = True
        break # Stop the loop after finding the first match
# Handle the case where x is greater than all values in the list
if not found:
    print("No value in the list is greater than or equal to x.")