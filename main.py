from stats import get_num_words
from stats import get_num_chars

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(f"{get_num_words(file_contents)} words found in the document")
    print(get_num_chars(file_contents))

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
