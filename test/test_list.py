from code.list import ListOperations
import unittest

class TestListOperations(unittest.TestCase):
    def setUp(self):
        # Initialize a test list
        self.test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

        # Create an instance of ListOperations with the test list
        self.list_ops = ListOperations(self.test_list)

    # Method to test getting the sum of all elements in the list
    def test_get_sum(self):
        self.assertEqual(self.list_ops.get_sum(), 44)

    # Method to test getting the average of all elements in the list
    def test_get_average(self):
        self.assertEqual(self.list_ops.get_average(), 4.0)

    # Method to test getting the minimum value in the list
    def test_get_min_value(self):
        self.assertEqual(self.list_ops.get_min_value(), 1)

    # Method to test getting the maximum value in the list
    def test_get_max_value(self):
        self.assertEqual(self.list_ops.get_max_value(), 9)

    # Method to test sorting the list in ascending order
    def test_sort_list(self):
        self.assertEqual(self.list_ops.sort_list(), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    # Method to test reversing the order of elements in the list
    def test_reverse_list(self):
        self.assertEqual(self.list_ops.reverse_list(), [5, 3, 5, 6, 2, 9, 5, 1, 4, 1, 3])

    # Method to test removing duplicates from the list
    def test_remove_duplicates(self):
        self.assertEqual(self.list_ops.remove_duplicates(), [1, 2, 3, 4, 5, 6, 9])

    # Method to test checking if a specified element is present in the list
    def test_element_in_list(self):
        self.assertTrue(self.list_ops.element_in_list(5))
        self.assertFalse(self.list_ops.element_in_list(7))

    # Method to test counting occurrences of a specified element in the list
    def test_count_element(self):
        self.assertEqual(self.list_ops.count_element(5), 3)
        self.assertEqual(self.list_ops.count_element(7), 0)

    # Method to test adding a new element to the end of the list
    def test_add_element(self):
        self.list_ops.add_element(7)
        self.assertEqual(self.list_ops.my_list, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 7])

    # Method to test removing the first occurrence of a specified element from the list
    def test_remove_element(self):
        self.list_ops.remove_element(5)
        self.assertEqual(self.list_ops.my_list, [3, 1, 4, 1, 9, 2, 6, 5, 3, 5])

if __name__ == '__main__':
    unittest.main()
