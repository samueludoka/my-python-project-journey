from unittest import TestCase

from chapter5_exercise import StringConcatenate


class Test(TestCase):
    def test_string_concatenate(self):
        given = 'abc'
        result = 'abcing'
        expected = StringConcatenate.string_concatenate(given)
        self.assertEqual(expected, result)

    def test_string_concatenate2(self):
        given = 'abcing'
        result = 'abcingly'
        expected = StringConcatenate.string_concatenate2(given)
        self.assertEqual(expected, result)

    def test_string_concatenate3(self):
        given = 'ab'
        result = 'ab'
        expected = StringConcatenate.String_concatenate3(given)
        self.assertEqual(expected, result)

