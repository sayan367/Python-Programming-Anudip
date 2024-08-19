def read_and_display_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"File {file_name} not found.")

read_and_display_file_content("/Users/sayansarkar/Desktop/Anudip/Module_15/sayan.txt")