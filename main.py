import sys
from stats import count_words
from stats import count_characters
from stats import sorted_dic


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    list_of_dictionaries = sorted_dic(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dic in list_of_dictionaries:
        if dic["char"].isalpha():
            print(f'{dic["char"]}: {dic["num"]}')
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
