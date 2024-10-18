import re

def only_dzongkha_word (word):
    return re.match (r"^[\u0F00-\u0FFF]+$", word)

def load_dzongkha_dictionary (dictionary_file):
    dzongkha_words = set()
    with open(dictionary_file, "r", encoding="utf-8") as file:
        for line in file:
            words = line.split()
            for word in words:
                if only_dzongkha_word(word):
                    dzongkha_words.add(word)
    return dzongkha_words

def check_incorrect_spellings(dictionary_file, script_file):
    dzongkha_words = load_dzongkha_dictionary(dictionary_file)
    with open(script_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    incorrect_spellings = []

    for line in lines:
        words = line.split()

        for word in words:
            if only_dzongkha_word(word) and word not in dzongkha_words:
                incorrect_spellings.append(word)

    return incorrect_spellings

dictionary_file = "dzo_dict.txt"  
script_file = "356.txt"

incorrect_spellings = check_incorrect_spellings(dictionary_file, script_file)

if incorrect_spellings:
    print("Incorrect Dzongkha spellings found:")
    for word in incorrect_spellings:
        print(word)
else:
    print("No incorrect spellings found.")
