from unittest import TestCase

from chapter5_exercise import change_char_string
from chapter5_exercise.change_char_string import dolapo


class Test(TestCase):

    def test_dolapo(self):
        word = 'restart'
        old_string = "r"
        new_string = "$"
        self.assertEqual('resta$t', dolapo(word, new_string, old_string))

