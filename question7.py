#Time Conversion Function
def convert_seconds_to_time(total_seconds):
    # 1. Input validation
    # Check that the input is a non-negative integer
    if not isinstance(total_seconds, int) or total_seconds < 0:
        return "Invalid input: Seconds must be a non-negative integer."
    # 2. Calculate hours, minutes, and seconds
    # Use modulo 24 to make sure hours stay within one day
    hours_24 = (total_seconds // 3600) % 24
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    # 3. Determine AM or PM and convert to 12-hour format
    suffix = "AM"
    if hours_24 >= 12:
        suffix = "PM"
        if hours_24 > 12:
            hours_12 = hours_24 - 12
        else:
            hours_12 = 12  # Exactly noon
    else:
        if hours_24 == 0:
            hours_12 = 12  # Midnight
        else:
            hours_12 = hours_24
    # 4. Return the formatted string
    # Format required by the assignment: "H M S AM/PM"
    return f"{hours_12} {minutes} {seconds} {suffix}"
# TEST_CODE
# 19007 seconds ≈ 5 hours 16 minutes 47 seconds AM
print(convert_seconds_to_time(19007))
# Afternoon example (14:00 = 50400 seconds)
print(convert_seconds_to_time(50400))
# Midnight (0 seconds)
print(convert_seconds_to_time(0))
