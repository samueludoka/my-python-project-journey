from unittest import TestCase

from chapter_4_exercises import biggest_odd
from chapter_4_exercises.biggest_odd import biggestOdd, bigger_odds


class Test(TestCase):
    def test_biggest_odd(self):
        numbers = '23569'
        answer = '9'
        result = biggestOdd(numbers)
        self.assertEqual(answer, result)

    def test_bigger_odds(self):
        numbers = '23569'
        answer = 9
        result = bigger_odds(numbers)
        self.assertEqual(answer, result)

    def test_bigger_odds(self):
        self.assertEqual(biggest_odd.bigger_odds('23495'), 9)
