def main():
    book_path = input("Enter the path to the book: ")
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    word_list = get_word_list(text)
    print(f"{word_count} words found in the document")
    print(word_list)
    alphabetic_characters, non_alphabetic_characters = get_character_count(text)
    sorted_alphabetic_characters = dict(sorted(alphabetic_characters.items()))
    print(sorted_alphabetic_characters)
    print(non_alphabetic_characters)

def get_word_count(text):
     words = text.split()
     return  len(words)

def get_word_list(text):
        word_list = {}
        words = text.lower().split()
        for word in words:
            word = word.strip(".,!?\"';:=()[]")
            if word in word_list:
                  word_list[word] += 1
            else:
             word_list[word] = 1
        return word_list

def get_book_text(path):
      with open(path) as f:
        return f.read()
      
def get_character_count(text):
    alphabetic_count = {}
    non_alphabetic_count = {}
    for char in text:
            char = char.lower()
            if 'a' <= char <= 'z': 
                if char in alphabetic_count:
                    alphabetic_count[char] += 1
                else:
                    alphabetic_count[char] = 1
            else:
                 non_alphabetic_count[char] =1

    return alphabetic_count, non_alphabetic_count

main()