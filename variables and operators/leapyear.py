def is_leap_year(year):
    # Check if the year is a multiple of 4 and (not a multiple of 100 or a multiple of 400)
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Accept year input from the user
year = int(input("Enter a year: "))

# Check if the entered year is a leap year and print the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
