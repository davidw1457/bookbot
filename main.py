from stats import get_num_words
from stats import get_num_chars
from stats import sort_dictionary
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    file_contents = get_book_text(book)
    word_count = get_num_words(file_contents)
    sorted_dictionary = sort_dictionary(get_num_chars(file_contents))
    print_report(book, word_count, sorted_dictionary)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book, count, chars):
    eq = "="
    hy = "-"
    print(f"{eq*12} BOOKBOT {eq*12}")
    print(f"Analyzing book found at {book}...")
    print(f"{hy*11} Word Count {hy*10}")
    print(f"Found {count} total words")
    print(f"{hy*9} Character Count {hy*7}")
    for char in chars:
        current = char["char"]
        if current.isalpha():
            count = char["num"]
            print(f"{current}: {count}")
    print(f"{eq*13} END {eq*15}")

main()
