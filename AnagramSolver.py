"""
Program: AnagramSolver.py
Author: Lily Ellison
Last Date Modified: 04/30/23

The purpose of this program is to create a gui that accepts letters from the user and returns all words that can be
made from those letters (words will have 3 letters or more)
"""

import itertools as it
import datetime
import tkinter



possible_words = []
input_letters = "fellows"
all_words_by_length = {}
real_words = []


with open('words_alpha.txt') as word_file:
    valid_words = set(word_file.read().split())


#Verify is word:
def is_word(w: str) -> bool:
    return w in valid_words


def words_from_num_letters(letters: str, num: int):
    real_words.clear()
    possible_words.clear()
    for item in list(it.permutations(letters, num)):
        possible_words.append(("".join(item)))
    for permutation in set(possible_words):
        if is_word(permutation):
            real_words.append(permutation)
    return real_words


def make_dictionary_by_number(letters: str):
    f = open('words.txt', 'a', encoding="utf-8")
    f.writelines(datetime.datetime.now().isoformat() + "\n")
    for number in range(3, len(letters)):
        words_to_add = words_from_num_letters(letters, number)
        all_words_by_length.update({str(number): str(words_to_add)})
        f.writelines(str(number) + ': ' + str(words_to_add) + "\n")
    return all_words_by_length


def words_from_all_letters(letters: str):
    for item in list(it.permutations(letters)):
        possible_words.append(("".join(item)))
    for permutation in set(possible_words):
        if is_word(permutation):
            real_words.append(permutation)
    return real_words


print(make_dictionary_by_number(input_letters))







