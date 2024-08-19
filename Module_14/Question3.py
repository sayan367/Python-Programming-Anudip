def count_cases(input_str):
    uppercase = lowercase = numbers = special = 0

    for char in input_str:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            numbers += 1
        else:
            special += 1

    print(f"UpperCase: {uppercase}")
    print(f"LowerCase: {lowercase}")
    print(f"NumberCase: {numbers}")
    print(f"SpecialCase: {special}")

# Example usage:
input_str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
count_cases(input_str)
