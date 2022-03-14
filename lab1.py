import os
import re
from statistics import median


def get_average_words_count(text):
    sentences = re.split(r"[.!?\n]\s", text)
    return sentences


def get_median_words_count(text):
    print(median([len(sentence.split()) for sentence in text.split(".")]))


def get_words(text):
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").\
        replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    return words


def sort_words(words):
    sort = sorted(words, key=lambda a: len(a))
    return sort


def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def get_top_ngrams(words, n, ktop):
    if not n:
        n = 4
    if not ktop:
        ktop = 10
    to_print_list = sort_words(words)
    print(to_print_list)
    for i in range(len(to_print_list), 0, -1):
        if int(ktop) > 0 and len(to_print_list[i - 1]) >= int(n):
            for j in range(0, int(n)):
                print(to_print_list[i - 1][j], end="")
            print("")
            ktop -= 1

def print_result(text, words, ktop, ngrams, words_dict):
    print(text)
    print(f"Кол-во слов: {get_words(text)}")
    print(f"Кол-во уникальных слов: {len(words_dict)}")
    print(f"Кол-во предложений: {len(get_average_words_count(text))}")
    print(f"Average count in sentence: "
          f"{len(words) / len(get_average_words_count(text))}")
    print(f"Median count in sentence: {get_median_words_count(text)}")
    get_top_ngrams(words, int(ngrams), int(ktop))
    print("Все использованные слова:")
    for word in words_dict:
        print(word.ljust(20), words_dict[word])


def main():
    filename = "/home/arkady/dev/python/test/text.txt"
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        with open(filename, encoding="utf8") as file:
            text = file.read()
        words = get_words(text)
        words_dict = get_words_dict(words)
        ngrams = input("Enter ngrams: ")
        ktop = input("Enter ngrams: ")
        print_result(text, words, ktop, ngrams, words_dict)


if __name__ == "__main__":
    main()
