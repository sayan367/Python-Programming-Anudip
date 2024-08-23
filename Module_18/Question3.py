try:
    file_name = input("Enter the file name to open: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist!")
