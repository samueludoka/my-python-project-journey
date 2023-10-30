from unittest import TestCase

from chapter_4_exercises import list_to_dictionary
from test.group_list_test import assertEquals


class Test(TestCase):
    def test_list_to_dictionary(self):
        score = ['apple', 'banana', 'coconut']
        expected = {'a': 'apple', 'b': 'banana', 'c': 'coconut'}
        result = list_to_dictionary.last_to_dictionary(score)
        assertEquals(expected, result)

    def test_two_list(self):
        input1 = ['a', 'b', 'c', 'd', 'e']
        input2 = [1, 2, 3, 4, 5]
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        result = list_to_dictionary.two_list_to_dictionary(input1, input2)
        assertEquals(expected, result)

    def test_difference(self):
        score = [70, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        expected = 70
        result = list_to_dictionary.difference_in_smallest_and_largest_in_a_list(score)
        assertEquals(expected, result)

    def test_frequency(self):
        elements = [1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 6, 7]
        expected = [1, 2, 5]
        result = list_to_dictionary.frequency(elements)
        assertEquals(expected, result)

    def test_remove_multiple_String(self):
        String_input = ["'ABC','xyz'", 'abc', 'xyz']
        String_output = ['ABC', 'xyz', 'abc', 'xyz']
        result = list_to_dictionary.remove_multiple_String(String_input)
        assertEquals(String_output, result)

    def test_Split_a_list(self):
        sample_input = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        expected = [10, 75, 20, 30, 15, 5], [5, 40, 25, 40, 35]
        result = list_to_dictionary.split_a_list(sample_input)
        assertEquals(expected, result)
