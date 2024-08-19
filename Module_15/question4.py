def display_short_words(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) < 4:
                        print(word)
    except FileNotFoundError:
        print(f"File {file_name} not found.")

display_short_words("/Users/sayansarkar/Desktop/Anudip/Module_15/sayan.txt")