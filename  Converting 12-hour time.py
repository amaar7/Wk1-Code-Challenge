    # Converts a 12-hour time to 24-hour time.
def convert_to_24_hour(hour, minute, period):

    # Convert hour based on the period (am/pm)
    if period.lower() == "am":
        if hour == 12:  # Handle midnight (12 am)
            hour = 0
    else:
        if hour != 12:  # Handle noon (12 pm)
            hour += 12

    # Return the time in 24-hour format as a four-digit string
    return f"{hour:02d}{minute:02d}"
