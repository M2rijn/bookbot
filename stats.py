def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def character_count(text):
    characters = {}
    for character in text.lower():
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(items):
    return items["num"]

def sorted_character_count(dictionary):
    sorted_characters = []
    for key, value in dictionary.items():
        if key.isalpha():
            sorted_characters.append({"char": key, "num": value})
    sorted_characters.sort(reverse=True, key=sort_on)
    return(sorted_characters)