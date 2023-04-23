from PyDictionary import PyDictionary
import itertools as it

dict1 = PyDictionary()
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
    for number in range(3, len(letters)):
        words_to_add = words_from_num_letters(letters, number)
        all_words_by_length.update({str(number): str(words_to_add)})



def words_from_all_letters(letters: str):
    for item in list(it.permutations(letters)):
        possible_words.append(("".join(item)))
    for permutation in set(possible_words):
        if is_word(permutation):
            real_words.append(permutation)
    return real_words

"""
def find_all_words(letters: str):
    max_len = len(letters)+1
    for num in range(3, max_len):
        value_list = words_from_num_letters(letters, num)
        all_words_by_length[num] = value_list
    return all_words_by_length
"""

make_dictionary_by_number(input_letters)

print(all_words_by_length.get("5"))









