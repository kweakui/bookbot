from stats import count_words
from stats import count_chars
from stats import chars_list
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents
     
def main():
    if len(sys.argv) < 2: #Check to make sure there is a file path
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1] #Pass the file path to the variable
    text = get_book_text(file_path)
    word_count = count_words(text)
    chars = count_chars(text)
    sorted_chars = chars_list(chars)

    
        

    # Print report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    
    # Print word count
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    # Print character count
    print("--------- Character Count -------")
    # Loop through the sorted characters
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    # Print report footer
    print("============= END ===============")

main()

    