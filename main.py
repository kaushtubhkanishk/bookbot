import sys
from stats import get_num_words, get_symbols, order_dict

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        book_data = file.read()
    
    return book_data

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_data = get_book_text(sys.argv[1])
    num_words = get_num_words(book_data)
    symbols_dict = get_symbols(book_data)

    list_dict = order_dict(symbols_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in list_dict:
        for key, item in i.items():
            print(f"{key}: {item}")
    print("============= END ===============")

if __name__ == "__main__":
    main()