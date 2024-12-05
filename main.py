def main():
    book_path = input("Enter the path to the book: ")
    text = get_book_text(book_path)
    #Calculations
    word_count = get_word_count(text)
    word_list = get_word_list(text)
    word_list_tuples = list(word_list.items())
    alphabetic_characters, non_alphabetic_characters = get_character_count(text)
    sorted_alphabetic_characters = dict(sorted(alphabetic_characters.items()))
    char_list = list(alphabetic_characters.items())
    sorted_char_list = (sorted(char_list, key=lambda x: x[1], reverse=True))
    sorted_word_list = (sorted(word_list_tuples, key=lambda x: x[1], reverse=True))
    # Printing Reports

    with open('report.txt', 'w') as file:
        with open('report.txt', 'w') as file:
            file.write('--- Begin report of your document ---\n')
            file.write(f'{word_count} words found in the document\n')
    
            for word, count in sorted_word_list:
                file.write(f"The word '{word}' occurs {count} times in the document\n")
        
            file.write('--- End report ---\n')

    print("--- Begin report of your document ---")
    print(f"{word_count} words found in the document")
    for char, count in sorted_char_list:
        print(f"The '{char}' character was found {count} times")
    for word, count in sorted_word_list:
         print(f"The word '{word}' was found {count} times")
    print("--- End report ---")
    print(f"Non-alphabetic characters: {non_alphabetic_characters}")
    print(f"Word list: {sorted_word_list}")
  
    #print(sorted_alphabetic_characters)
    #print(non_alphabetic_characters)
  

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