"""
Program: AnagramSolver.py
Author: Lily Ellison
Last Date Modified: 04/30/23

The purpose of this program is to create a gui that accepts letters from the user and returns all words that can be
made from those letters (words will have 3 letters or more)
"""

import itertools as it
import datetime
import tkinter as tk


class WordFinderGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.instruction_label = tk.Label(self.root, text="Please enter the letters you would like made into words: ",
                                          font=('Times New Roman', 16))
        self.instruction_label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Times New Roman', 14))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Create file with words", font=('Times New Roman', 14),
                                    variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.find_words_button = tk.Button(self.root, text="Find Words", font=('Times New Roman', 16),
                                           command=self.get_words)
        self.find_words_button.pack(padx=10, pady=10)

        self.results_label = tk.Label(self.root, text="Results will appear here.", font=('Times New Roman', 14))
        self.results_label.pack(padx=10, pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", font=('Times New Roman', 16), command=self.exit)
        self.exit_button.pack(padx=10, pady=10)

        self.root.mainloop()

    def get_words(self):
        if self.check_input(self.textbox.get('1.0', tk.END)):
            self.results_label.config(text="Processing.")

        else:
            pass


    def exit(self):
        self.root.destroy()


        # Create file or not: if self.check_state.get() == 0: <- no file

       # else:
            #create txt file
            #To get textbox info: self.textbox.get('1.0', tk.END)



    possible_words = []

    real_words = []
    input_letters = ""

    def is_valid_input(self, filtered_input):
        return len(filtered_input) > 3

    def check_input(self, il):
        valid_letters = ""
        valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        for letter in il:
            if valid_characters.issuperset(letter):
                valid_letters += letter
        if self.is_valid_input(valid_letters):
            to_output = self.make_dictionary_by_number(valid_letters)
            self.results_label.config(text=str(to_output))

        else:
            self.results_label.config(text="Invalid entry. Please enter only letters.")




    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())


#Verify is word:
    def is_word(self, w: str) -> bool:
        return w in self.valid_words


    def words_from_num_letters(self, letters: str, num: int):
        self.real_words.clear()
        self.possible_words.clear()
        for item in list(it.permutations(letters, num)):
            self.possible_words.append(("".join(item)))
        for permutation in set(self.possible_words):
            if self.is_word(permutation):
                self.real_words.append(permutation)
        return self.real_words


    def make_dictionary_by_number(self, letters: str):
        all_words_by_length = {}
        f = open('words.txt', 'a', encoding="utf-8")
        f.writelines(datetime.datetime.now().isoformat() + "\n")
        for number in range(3, len(letters)):
            words_to_add = self.words_from_num_letters(letters, number)
            all_words_by_length.update({str(number): str(words_to_add)})

            f.writelines(str(number) + ': ' + str(words_to_add) + "\n")
        return all_words_by_length


    def words_from_all_letters(self, letters: str):
        for item in list(it.permutations(letters)):
            self.possible_words.append(("".join(item)))
        for permutation in set(self.possible_words):
            if self.is_word(permutation):
                self.real_words.append(permutation)
        return self.real_words




WordFinderGUI()





