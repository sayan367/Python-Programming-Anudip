import re

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[@#$%^&+=]", password):
        return False
    return True

# Example usage:
password = input("Enter a password: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. It must be at least 8 characters long, contain at least one lowercase letter, one uppercase letter, one digit, and one special character.")
