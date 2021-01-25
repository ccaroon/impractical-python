#!/bin/env python
"""Pig Latin Translator"""

VOWELS = ('a','e','i','o','u')

def is_igpay_atinlay(sentence):
    """Detect if a sentence is in Pig Latin"""

    is_igpay = True
    words = sentence.split()
    for word in words:
        if not word.endswith('ay'):
            is_igpay = False
            break

    return is_igpay

def igpay_otay_englishway(sentence):
    """Translate from Pig Latin to English"""

    words = sentence.split()
    new_words = []
    for word in words:
        # Word started with a vowel
        # TODO: what abuot "ishway" == "wish"
        if word.endswith('way'):
            new_words.append(word[0:-3])
        else:
            # raigcay
            first_char = word[-3]
            new_words.append(F"{first_char}{word[0:-3]}")

    return ' '.join(new_words).title()

def englishway_otay_igpay(sentence):
    """Translate from English to Pig Latin"""

    words = sentence.split()
    new_words = []
    for word in words:
        if word.lower().startswith(VOWELS):
            new_words.append(F"{word}way")
        else:
            first_char = word[0]
            new_word = word.lstrip(first_char)
            new_words.append(F"{new_word}{first_char}ay")

    return ' '.join(new_words).title()

def main():
    """Entry Point"""
    sentence = input("Translate> ")

    translation = None
    if is_igpay_atinlay(sentence):
        translation = igpay_otay_englishway(sentence)
    else:
        translation = englishway_otay_igpay(sentence)

    print("---=== Translation ===---")
    print(translation)

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
