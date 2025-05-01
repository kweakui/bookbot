from stats import count_words
from stats import count_chars

def get_book_text(file_path): #open file and return contents of the file as a string
    with open(file_path) as file: #Open the file
        file_contents = file.read() #read the contents
        return file_contents
     
def main():
    text = get_book_text("books/frankenstein.txt")
    count = count_words(text)
    chars = count_chars(text)
    print(count,"words found in the document")
    print(chars)

main()

    