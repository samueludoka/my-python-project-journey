import unittest

from list_assignment.tuple_corn_flakes import reverse_list, get_integer, offload_element, rearrange_list


class MyTestCase(unittest.TestCase):
    def test_reverse_list(self):
        list = (10, 20, 30, 40, 50, 70, 80)
        answer = (80, 70, 50, 40, 30, 20, 10)
        result = reverse_list(list)
        self.assertEqual(answer, result)

    def test_get_integer(self):
        list = ("orange", [10, 20, 30], (5, 15, 25))
        answer = ((1, 20), (2, 25))
        result = get_integer(list)
        self.assertEqual(answer, result)

    def test_unpack_element(self):
        list = 15, 25, 60, 50, 30, 40, 45, 55
        answer = (55, 15)
        result = offload_element(list)
        self.assertEqual(answer, result)


    def test_sort_turple(self):
        number = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
        answer = (('c', 11), ('a', 23), ('d', 29), ('b', 37))
        result = rearrange_list(number)
        self.assertEqual(answer, result)





if __name__ == '__main__':
    unittest.main()
