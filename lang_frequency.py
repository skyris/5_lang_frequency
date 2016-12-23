import os
from string import punctuation
from sys import argv


def load_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError("No such file: {}".format(filepath))
    with open(filepath, "r") as file_handler:
        return file_handler.read()


def replace_punctuation(text):
    for sign in punctuation.replace("-", ""):
        text = text.replace(sign, "")
    return text.replace(" - ", " ")


def get_most_frequent_words(text):
    words_dictionary = {}
    for word in text.split():
        words_dictionary[word] = words_dictionary.get(word, 0) + 1
    return sorted(words_dictionary, key=lambda current_word: words_dictionary[current_word], reverse=True)[:10]


if __name__ == '__main__':
    if len(argv) != 2:
        print("Ввидите имя загружаемого текстового файла после 'python3 {}'".format(__file__))
        exit()
    if argv[1] == "--help":
        print("Поместите в текущую директорию текстовый файл.")
        print("Наберите python3 {} <имя файла> и нажмите enter.".format(__file__))
        exit()

    filename = argv[1]
    raw_text = load_data(filename)
    prepared_text = replace_punctuation(raw_text)
    print(get_most_frequent_words(prepared_text))
