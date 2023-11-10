from unittest import TestCase

from chibuzo_assignment import pizza_hut


class Test(TestCase):
    def test_box_size(self):
        box_size = "LARGE"
        result = 10
        expected = pizza_hut.box_size(box_size)
        self.assertEqual(expected, result)

    def test_number_of_hungry_persons(self):
        super_hungry = 6
        normal_hungry = 5
        classic_hungry = 3
        result = 37
        expected = pizza_hut.number_of_hungry_persons(super_hungry, normal_hungry, classic_hungry)
        self.assertEqual(expected, result)

    def test_number_of_slices(self):
        super_hungry = 8
        normal_hungry = 4
        classic_hungry = 7
        result = 47
        expected = pizza_hut.number_of_slices(super_hungry, normal_hungry, classic_hungry)
        self.assertEqual(expected, result)

    def test_number_of_boxes(self):
        super_hungry = 8
        normal_hungry = 4
        classic_hungry = 7
        large_box = 4.7
        expected = pizza_hut.number_of_boxes(super_hungry, normal_hungry, classic_hungry, large_box)
        self.assertEqual(expected, large_box)

    def test_number_of_slices_left(self):
        super_hungry = 8
        normal_hungry = 4
        classic_hungry = 7
        large_box = 2
        expected = pizza_hut.number_of_boxes(super_hungry, normal_hungry, classic_hungry, large_box)
        self.assertEqual(expected, large_box)


    def test_boxes_total_amount(self):
        super_hungry = 8
        normal_hungry = 4
        classic_hungry = 7
        large_box = 200000
        expected = pizza_hut.number_of_boxes(super_hungry, normal_hungry, classic_hungry, large_box)
        self.assertEqual(expected, large_box)