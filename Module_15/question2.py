def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            words = file.read().split()
            print(f"Total number of words: {len(words)}")
    except FileNotFoundError:
        print(f"File {file_name} not found.")

count_words_in_file("/Users/sayansarkar/Desktop/Anudip/Module_15/sayan.txt")