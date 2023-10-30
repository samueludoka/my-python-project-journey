from unittest import TestCase, result

from chapter_4_exercises.Equal_string import equalStrings


class Test(TestCase):
    def test_equal_strings(self):
        weed = 'love'
        lewd = 'evol'
        answer = 'love' == 'evol'
        result = equalStrings(weed, lewd)
        self.assertTrue(result)



