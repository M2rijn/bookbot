import sys
from stats import get_book_text, word_count, character_count, sorted_character_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    num_characters = character_count(book_text)
    sorted_characters = sorted_character_count(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_characters:
        print(f'{dictionary["char"]}: {dictionary["num"]}')
    print("============= END ===============")

main()