def count_uppercase_chars_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            uppercase_chars = sum(1 for char in content if char.isupper())
            print(f"Total uppercase characters: {uppercase_chars}")
    except FileNotFoundError:
        print(f"File {file_name} not found.")

count_uppercase_chars_in_file("/Users/sayansarkar/Desktop/Anudip/Module_15/sayan.txt")