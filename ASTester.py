"""
Program: ASTester.py
Author: Lily Ellison
Last Date Modified: 05/01/23

The purpose of this program is to test the AnagramSolver.py program.

"""
import tkinter
import unittest

import _tkinter

import AnagramSolver as anagram


class TKinterTestCase(unittest.TestCase):
    def test_setup(self):
        self.root = tkinter.Tk()
        self.pump_events()


    def tearDown(self) -> None:
        if self.root:
            self.root.destroy()
            self.pump_events()

    def pump_events(self):
        while self.root.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
            pass


class ASTester(TKinterTestCase):
    def valid_input_test(self):
        wf = anagram.WordFinderGUI()
        self.assertTrue(wf.is_valid_input("add"))

    def invalid_input_test(self):
        wf = anagram.WordFinderGUI()
        self.assertFalse(wf.is_valid_input("666"))

    def get_words_test(self):
        wf = anagram.WordFinderGUI()
        self.assertEqual(wf.get_words(), "")

    def check_input_test(self):
        wf = anagram.WordFinderGUI()
        self.assertTrue("3: ['add', 'dad']" in wf.check_input("add"))



    def run_all_tests(self):
        self.valid_input_test()
        self.invalid_input_test()
        self.get_words_test()
        self.check_input_test()



if __name__ == '__main__':
    unittest.main()
    ASTester.run_all_tests()


