#!/bin/env python
"""Open a list of words and search for palindromes"""

import sys

WORD_LIST = "/usr/share/dict/words"
# ------------------------------------------------------------------------------
def find_palindromes(word_file, min_length=2):
    """Find Palindromes in word list"""
    found_list = []
    try:
        with open(word_file, "r") as file:
            word = " "
            while word:
                word = file.readline().strip()
                if len(word) < min_length:
                    continue

                if word == word[::-1]:
                    found_list.append(word)
    except OSError as err:
        print(err)

    return found_list
# ------------------------------------------------------------------------------
def main():
    """
    Usage: find_palindromes.py WORD_LIST MIN_LENTH

    * WORD_LIST - Name of the file to read the word list from.
    * MIN_LENGTH - Words must be of length MIN_LENGTH to count. Defaults to 2.

    Examples:
        * bash> find_palindromes.py
            - Find palindromes in default word list of at least 2 chars.
        * bash> find_palindromes.py /tmp/my-word-list.txt
            - Find palindromes in /tmp/my-word-list.txt of at least 2 chars.
        * bash> find_palindromes.py /tmp/my-word-list.txt 4
            - Find palindromes in /tmp/my-word-list.txt of at least 4 chars.
    """
    min_len = 2
    word_list = WORD_LIST

    arg_count = len(sys.argv)

    if arg_count == 2:
        word_list = sys.argv[1]
    elif arg_count == 3:
        word_list = sys.argv[1]
        min_len = int(sys.argv[2])

    palindromes = find_palindromes(word_list, min_len)
    count = len(palindromes)
    for word in palindromes:
        print(word)
    print(F"Found {count} palindromes in {word_list} at least {min_len} characters long.")
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
