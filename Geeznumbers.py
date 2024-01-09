# Define the Geez numerals as a dictionary
geez_numerals = {
    1: "፩",
    2: "፪",
    3: "፫",
    4: "፬",
    5: "፭",
    6: "፮",
    7: "፯",
    8: "፰",
    9: "፱",
    10: "፲",
    20: "፳",
    30: "፴",
    40: "፵",
    50: "፶",
    60: "፷",
    70: "፸",
    80: "፹",
    90: "፺",
    100: "፻",
    10000: "፼"
}

# Define a function to convert Arabic numerals to Geez numerals
def arabic_to_geez(num):
    # Check if the input is a valid integer
    try:
        num = int(num)
    except ValueError:
        return "Invalid input"

    # Check if the input is in the range of 1 to 99999999
    if num < 1 or num > 99999999:
        return "Out of range"

    # Initialize an empty string to store the output
    output = ""

    # Special case for numbers in the hundreds
    if 100 <= num < 10000:
        hundreds, num = divmod(num, 100)
        if hundreds > 1:
            output += arabic_to_geez(hundreds)  # Recursive call for hundreds
        output += geez_numerals[100]
        # Check if the number is divisible by 100
        if num == 0:
            return output

    # Special case for numbers in the thousands
    if 10000 <= num < 1000000:
        thousands, num = divmod(num, 10000)
        if thousands > 1:
            output += arabic_to_geez(thousands)  # Recursive call for thousands
        output += geez_numerals[10000]
        # Check if the number is divisible by 10000
        if num == 0:
            return output

    # Special case for numbers in the millions
    if num >= 1000000:
        millions, num = divmod(num, 1000000)
        if millions > 1:
            output += arabic_to_geez(millions)  # Recursive call for millions
        output += geez_numerals[100] + geez_numerals[10000]
        # Check if the number is divisible by 1000000
        if num == 0:
            return output

    # Loop through the Geez numerals in descending order
    for key in sorted(geez_numerals.keys(), reverse=True):
        # Divide the input by the current key and get the quotient and remainder
        quotient, remainder = divmod(num, key)
        # If the quotient is positive, append the corresponding Geez numeral to the output
        if quotient > 0:
            output += geez_numerals[key] * quotient
        # Update the input to the remainder
        num = remainder
        # Check if the number is divisible by 10
        if num == 0 and key == 10:
            output += geez_numerals[10]

    # Return the output
    return output

# Take input from the command line
num = input("Enter a number: ")

# Convert the input to Geez numerals and print the result
print(arabic_to_geez(num))
