def print_line(character):
    """
    Prints a line of the specified character.
    
    Parameters:
    character (str): The character to print the line with. Should be a single character.
    """
    if len(character) != 1:
        raise ValueError("The input must be a single character.")
    print(character * 50)  # Prints a line of 50 characters

def calculate_SI(principal, rate_of_interest, terms):
    """
    Calculates the Simple Interest (SI) based on the principal, rate of interest, and number of years.
    
    Parameters:
    principal (float): The principal amount.
    rate_of_interest (float): The rate of interest per year (in percentage).
    terms (int): The number of years.
    
    Returns:
    float: The calculated simple interest.
    """
    # Simple Interest Formula: SI = (Principal * Rate * Time) / 100
    simple_interest = (principal * rate_of_interest * terms) / 100
    return simple_interest

print_line("$")
# Calculate Simple Interest
principal = 10000  # Example principal amount
rate_of_interest = 5  # Example rate of interest (5%)
terms = 3  # Example number of years

si = calculate_SI(principal, rate_of_interest, terms)
print(f"Simple Interest: {si}")