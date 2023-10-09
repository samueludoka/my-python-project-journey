import unittest

from chapter_three_assignment.divine import add_function, multiply_function, max_function, no_duplicate, triple_3x
from chapter_three_assignment import divine


def min_function(number):
    pass


class MyTestCase(unittest.TestCase):
    def test_add_function(self):
        number = [15, 20, 25, 20, 10, 5]
        answer = 95
        result = add_function(number)
        self.assertEqual(answer, result)

    def test_multiply_function(self):
        number = [15, 20, 25, 20, 10, 5]
        answer = 7500000
        result = multiply_function(number)
        self.assertEqual(answer, result)

    def test_max_function(self):
        number = [15, 20, 25, 20, 10, 5]
        answer = 25
        result = max_function(number)
        self.assertEqual(answer, result)

    def test_min_function(self):
        number = [15, 20, 25, 20, 10, 5]
        answer = 5

        self.assertEqual(answer, divine.min_function(number))

    def test_no_duplicate(self):
        number = [15, 20, 25, 20, 10, 5]
        answer = [15, 20, 25, 10, 5]
        result = no_duplicate(number)
        self.assertEqual(answer, divine.min_function(number))

    def test_triple_3x(self):
        number = [3, 7, 2, 6, 5]
        answer = [27, 343, 8, 216, 125]

        self.assertEqual(answer, divine.triple_function(number))



if __name__ == '__main__':
    unittest.main()
