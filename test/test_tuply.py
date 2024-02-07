import unittest
from code.tuple import TupleOperations

class TestTupleOperations(unittest.TestCase):
    def setUp(self):
        # Initialize a test tuple
        self.test_tuple = (1, 2, 3, 4, 5)
        # Create an instance of TupleOperations with the test tuple
        self.tuple_ops = TupleOperations(self.test_tuple)

    # Method to test getting the length of the tuple
    def test_get_length(self):
        self.assertEqual(self.tuple_ops.get_length(), 5)

    # Method to test concatenating two tuples
    def test_concatenate_tuples(self):
        other_tuple = (6, 7, 8)
        self.assertEqual(self.tuple_ops.concatenate_tuples(other_tuple), (1, 2, 3, 4, 5, 6, 7, 8))

    # Method to test counting occurrences of a specified element in the tuple
    def test_count_element(self):
        self.assertEqual(self.tuple_ops.count_element(3), 1)

    # Method to test checking if a specified element is present in the tuple
    def test_element_in_tuple(self):
        self.assertTrue(self.tuple_ops.element_in_tuple(4))
        self.assertFalse(self.tuple_ops.element_in_tuple(9))

    # Method to test converting the tuple to a set
    def test_convert_to_set(self):
        self.assertEqual(self.tuple_ops.convert_to_set(), {1, 2, 3, 4, 5})

if __name__ == "__main__":
    unittest.main()
