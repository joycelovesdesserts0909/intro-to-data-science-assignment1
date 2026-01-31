#ControlledMultiplicationLoop
#1. Set the limit value
threshold = 999
#Start values
product = 1
current_number = 1
#2. Loop while product is not greater than the threshold
while product <= threshold:
    # Multiply current_number into product
    product = product * current_number
    # If product is greater than threshold, stop the loop
    if product > threshold:
        break
    # Increase current_number for the next loop
    current_number = current_number + 1
#3. Print the final result
print(f"The final product is: {product}")
print(f"The number that caused the product to exceed the threshold is: {current_number}")