import unittest

from chapter_4_exercises.group_list import list_numbers, scores_odd, double_odd_numbers, change_some_elements


def assertEquals(answer, result):
    pass





class MyTestCase(unittest.TestCase):
    def test_numbers(self):
        numbers = list(range(1, 21))
        answer = list(range(1, 21))
        result = list_numbers(numbers)
        assertEquals(answer, result)

    def test_odd_numbers(self):
        numbers = list(range(1, 21))
        answer = list(range(1, 21, 2))
        result = scores_odd(numbers)
        assertEquals(answer, result)

    def test_double_odd_numbers(self):
        numbers = list(range(1, 21))
        answer = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42]
        result = double_odd_numbers(numbers)
        assertEquals(answer, result)

    def test_remove_some_elements(self):
        numbers = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42]
        answer = [2, 6, 10, 14, 0, 0, 0, 0, 34, 38, 42]
        result = change_some_elements(numbers)
        assertEquals(answer, result)

if __name__ == '__main__':
    unittest.main()
