import unittest

from chibuzo_assignment.ArrayFunctions import listLargest, reverse_a_list, odd_number_in_a_list, even_number_in_a_list, \
    element_exist_in_a_list, running_total, stringPalindrome, totalOfList, concatenate, combines_two_list, \
    combine_two_list


class MyTestCase(unittest.TestCase):
    def test_largestNumber(self):
        lists = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        answer = 10
        result = listLargest(lists)
        self.assertEqual(result, answer)

    def test_reverse_a_list(self):
        lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        answer = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = reverse_a_list(lists)
        self.assertEqual(result, answer)

    def test_0dd_Numbers_in_a_list(self):
        lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        answer = [1, 3, 5, 7, 9]
        result = odd_number_in_a_list(lists)
        self.assertEqual(result, answer)

    def test_even_numbers_in_a_list(self):
        lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        answer = [2, 4, 6, 8, 10]
        result = even_number_in_a_list(lists)
        self.assertEqual(result, answer)

    def test_an_element_exist_in_a_list(self):
        lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        answer = {3}
        result = element_exist_in_a_list(lists)
        self.assertEqual(result, answer)

    def test_running_total(self):
        lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        answer = 55
        result = running_total(lists)
        self.assertEqual(result, answer)

    def test_stringPalindrome(self):
        lists = "mom"
        result = stringPalindrome(lists)
        self.assertTrue(result)

    def test_totalOfList(self):
        lists = [10, 20, 30, 40, 50, 60, 70, 80]
        answer = 360
        result = totalOfList(lists)
        self.assertEqual(result, answer)

    def test_concatenate(self):
        list1 = [1, 2, 3]
        list2 = ["a", "b", "c"]
        answer = [1, 2, 3, "a", "b", "c"]
        result = concatenate(list1, list2)
        self.assertEqual(result, answer)

    def test_combine_two_list(self):
        list1 = [1, 2, 3]
        list2 = ["a", "b", "c"]
        answer = [1, "a", 2, "b", 3, "c"]
        result = combine_two_list(list1, list2)
        self.assertEqual(result, answer)



        # add assertion here


if __name__ == '__main__':
    unittest.main()
