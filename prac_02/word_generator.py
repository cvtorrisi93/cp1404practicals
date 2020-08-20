"""
CP1404/CP5632 - Practical - Christian Torrisi
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALL_LETTERS = VOWELS + CONSONANTS
FORMAT = "#%*"

word_format_length = random.randint(3, 10)
word_format = ""
for i in range(word_format_length):
    word_format += random.choice(FORMAT)

print("The word format is: {}".format(word_format))

word = ""

for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    else:
        word += random.choice(ALL_LETTERS)

print("The 'word' is {}".format(word))
