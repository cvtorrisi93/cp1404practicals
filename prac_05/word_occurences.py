"""
CP1404/CP5632 Practical - Christian Torrisi
Do-from-scratch - find each word and in a string
and count how many times it occurs
"""

words_to_count = {}

sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    if word in words_to_count:
        words_to_count[word] += 1
    else:
        words_to_count[word] = 1

words = list(words_to_count.keys())
words.sort()

max_word_length = len(max(words, key=len))

for word in words_to_count:
    print("{:{max_word_length}} : {}".format(word, words_to_count[word], max_word_length=max_word_length))