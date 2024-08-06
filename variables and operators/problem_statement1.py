#Problem statement 1
#A company decided to give a bonus of 5% to an employee if his/her year of
#service is more than 5 years .Ask users for their salary and year of service and
#print the net bonus amount.



def calculate_bonus(salary, years_of_service):
    if years_of_service > 5:
        bonus = 0.05 * salary #5/100
    else:
        bonus = 0
    return bonus

# Accept salary and years of service input from the user
salary = float(input("Enter the employee's salary: "))
years_of_service = int(input("Enter the employee's years of service: "))

# Calculate and print the net bonus amount
bonus = calculate_bonus(salary, years_of_service)
print(f"The net bonus amount is: {bonus}")
