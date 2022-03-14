# Программа подсчета слов в файле
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
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def get_top_ngrams(text, n=4, ktop=10):
    result = {}

    def count_anagrams(word: str):
        word_len = len(word)

        for i in range(word_len):
            if i + n > word_len:
                break

            anagram = word[i:i + n]
            result[anagram] = text.count(anagram)

        # creating a dict of n-grams
    for word in text:
        count_anagrams(word)

        # getting top k of n-grams
    while len(result) > ktop:
        result_keys = list(result.keys())
        min_key = result_keys[0]

        for key in result_keys[1:]:
            if result[key] < result[min_key]:
                min_key = key

        result.pop(min_key)

    return result


def main():
    filename = "/home/arkady/dev/python/test/text.txt"
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        with open(filename, encoding="utf8") as file:
            text = file.read()
        words = get_words(text)
        words_dict = get_words_dict(words)
        print(text)
        print(f"Кол-во слов: {len(words)}")
        print(f"Кол-во уникальных слов: {len(words_dict)}")
        print(f"Кол-во предложений: {len(get_average_words_count(text))}")
        print(f"Кол-во предложений: {get_average_words_count(text)}")
        print(f"Average count in sentence: {len(words)/len(get_average_words_count(text))}")
        print(f"Median count in sentence: ", end=" ")
        get_median_words_count(text)
        print("top: ", get_top_ngrams(words))
        print("Все использованные слова:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":
    main()
