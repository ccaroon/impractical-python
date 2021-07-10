#! /usr/bin/env python
""" Input a word and find the anagrams """

import json
import os
import sys


WORD_LIST_JSON = F"{os.getenv('HOME')}/local/dict/words-466k.json"
################################################################################
def load_json(filename):
    """ Load a JSON file """

    data = []
    with open(filename, "r") as file:
        data = json.load(file)

    return data
################################################################################
def main():
    """ Entry Point """
    words = load_json(WORD_LIST_JSON)

    if len(sys.argv) > 1:
        user_word = sys.argv[1]
    else:
        user_word = input("Enter a word: ")

    user_word = user_word.lower()

    is_word = words.get(user_word, False)
    if is_word:
        anagrams = []
        word_chars = sorted(user_word)

        for (a_word, _) in words.items():
            if len(a_word) == len(user_word) and a_word != user_word:
                a_word_chars = sorted(a_word)
                if a_word_chars == word_chars:
                    anagrams.append(a_word)

        if anagrams:
            print(*anagrams, sep=', ')
        else:
            print(F"No anagrams of '{user_word}' found.")
    else:
        print(F"'{user_word}' is not a know word.")

################################################################################
if __name__ == "__main__":
    main()
