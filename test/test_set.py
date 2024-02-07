import unittest
from code.set import SetOperations

class TestSetOperations(unittest.TestCase):
    def setUp(self):
        # Initialize a test set
        self.test_set = {1, 2, 3, 4, 5}
        # Create an instance of SetOperations with the test set
        self.set_ops = SetOperations(self.test_set)

    # Method to test getting the length of the set
    def test_get_length(self):
        self.assertEqual(self.set_ops.get_length(), 5)

    # Method to test adding a new element to the set
    def test_add_element(self):
        self.set_ops.add_element(6)
        self.assertEqual(self.set_ops.my_set, {1, 2, 3, 4, 5, 6})

    # Method to test removing an element from the set
    def test_remove_element(self):
        self.set_ops.remove_element(3)
        self.assertEqual(self.set_ops.my_set, {1, 2, 4, 5})

    # Method to test checking if a specified element is present in the set
    def test_element_in_set(self):
        self.assertTrue(self.set_ops.element_in_set(4))
        self.assertFalse(self.set_ops.element_in_set(7))

    # Method to test getting the union of two sets
    def test_union_sets(self):
        other_set = {4, 5, 6, 7}
        self.assertEqual(self.set_ops.union_sets(other_set), {1, 2, 3, 4, 5, 6, 7})

    # Method to test getting the intersection of two sets
    def test_intersection_sets(self):
        other_set = {4, 5, 6, 7}
        self.assertEqual(self.set_ops.intersection_sets(other_set), {4, 5})

    # Method to test getting the difference between two sets
    def test_difference_sets(self):
        other_set = {4, 5, 6, 7}
        self.assertEqual(self.set_ops.difference_sets(other_set), {1, 2, 3})

if __name__ == "__main__":
    unittest.main()