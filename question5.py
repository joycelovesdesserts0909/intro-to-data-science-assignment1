#Circle Area Comparison with Validation
import math # Math library to get the value of pi
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    #1. Input validation
    # Check that both radii are integers and greater than 0
    if not (isinstance(radiusOfCircle1, int) and radiusOfCircle1 > 0 and
            isinstance(radiusOfCircle2, int) and radiusOfCircle2 > 0):
        # If the input is invalid, return an error message
        return "Invalid input: Radii must be positive integers."
    #2. Compute the areas of the two circles (Formula: pi * r^2)
    area1 = math.pi * (radiusOfCircle1 ** 2)
    area2 = math.pi * (radiusOfCircle2 ** 2)
    #3. Determine the larger and smaller circle areas (Use max() and min() for simplicity)
    larger_area = max(area1, area2)
    smaller_area = min(area1, area2)
    #4. Calculate the percentage coverage
    percentage = (smaller_area / larger_area) * 100
    #5. Return the result
    return percentage
#Test Cases
# Case 1: Valid input (example: r = 10 and r = 5)
# Area of r = 5 is 1/4 of area of r = 10 -> expected result: 25%
print("Test Case 1 (Valid):", circleAreaCoverage(10, 5))
# Case 2: Invalid input (negative number)
print("Test Case 2 (Invalid - Negative):", circleAreaCoverage(10, -5))
# Case 3: Invalid input (float number)
print("Test Case 3 (Invalid - Float):", circleAreaCoverage(10, 5.5))