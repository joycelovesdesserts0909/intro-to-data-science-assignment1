#Safe Function Application
#1. Define a function to compute power (x ** y)
def power_function(base, exponent):
    return base ** exponent
#2. Input data (list of number pairs)
# Added [10, -2] to test that negative exponents are skipped
pairs = [[5, 2], [3, 1], [4, 3], [2, 0], [10, -2]]
#3. List to store valid results
valid_results = []
#4. Loop with argument unpacking
#Instead of "for pair in pairs", we use "for x, y in pairs"
#x gets the base, y gets the exponent
for x, y in pairs:
    # Check the condition: exponent must be non-negative
    if y >= 0:
        # Call the power function
        result = power_function(x, y)
        # Add the result to the list
        valid_results.append(result)
    # If y < 0, the loop skips this pair automatically
#5. Print the final results
print(f"Original pairs: {pairs}")
print(f"Valid computed results: {valid_results}")