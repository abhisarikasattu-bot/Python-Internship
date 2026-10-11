# Task 2: Word Counter Program

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"\n--- File Analysis Result ---")
            print(f"Total Words in '{file_path}': {word_count}\n")
    except FileNotFoundError:
        print(f"\nError: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    print("=== Welcome to Word Counter ===")
    file_name = input("Enter the name of the text file (e.g., sample.txt): ")
    count_words(file_name)