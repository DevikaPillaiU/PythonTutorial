user_year = int(input("Enter a year: "))

def determine_leap_year(year_input):
    if (year_input % 4 == 0 and year_input % 100 != 0) or (year_input % 400 == 0):
        return f"{year_input} is a Leap Year."
    else:
        return f"{year_input} is NOT a Leap Year."

output = determine_leap_year(user_year)
print(output)

