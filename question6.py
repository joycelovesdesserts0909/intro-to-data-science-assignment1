#Distribution Analysis
def calculate_distribution(numbers):
    #1. Get unique values and sort them
    # set(numbers): remove duplicate values
    # sorted(...): sort values from smallest to largest
    unique_sorted_keys = sorted(list(set(numbers)))
    #2. Get the total number of elements in the original list
    total_count = len(numbers)
    #3. Create the result dictionary
    result = {}
    #4. Loop through each sorted unique key
    for key in unique_sorted_keys:
        # Count how many numbers in the original list (are less than or equal to the current key)
        count = sum(1 for x in numbers if x <= key)
        # Calculate the percentage
        percentage = (count / total_count) * 100
      # Store the result in the dictionary
        result[key] = percentage
    #Return the final dictionary
    return result
# TEST_CODE
input_numbers = [3, 1, 2, 3, 4, 2]
output = calculate_distribution(input_numbers)
# Print the result
print("Input:", input_numbers)
print("Distribution Dictionary:", output)