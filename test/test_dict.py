import unittest
from code.dict import DictionaryOperations

class TestDictionaryOperations(unittest.TestCase):
    def setUp(self):
        # Initialize a test dictionary
        self.test_dict = {'a': 1, 'b': 2, 'c': 3}
        # Create an instance of DictionaryOperations with the test dictionary
        self.dict_ops = DictionaryOperations(self.test_dict)

    # Method to test getting the keys of the dictionary
    def test_get_keys(self):
        self.assertEqual(self.dict_ops.get_keys(), ['a', 'b', 'c'])

    # Method to test getting the values of the dictionary
    def test_get_values(self):
        self.assertEqual(self.dict_ops.get_values(), [1, 2, 3])

    # Method to test checking if a specified key is present in the dictionary
    def test_key_in_dict(self):
        self.assertTrue(self.dict_ops.key_in_dict('b'))
        self.assertFalse(self.dict_ops.key_in_dict('d'))

    # Method to test checking if a specified value is present in the dictionary
    def test_value_in_dict(self):
        self.assertTrue(self.dict_ops.value_in_dict(2))
        self.assertFalse(self.dict_ops.value_in_dict(4))

    # Method to test adding a new key-value pair to the dictionary
    def test_add_key_value(self):
        self.dict_ops.add_key_value('d', 4)
        self.assertEqual(self.dict_ops.my_dict, {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    # Method to test removing a key-value pair from the dictionary
    def test_remove_key_value(self):
        self.dict_ops.remove_key_value('b')
        self.assertEqual(self.dict_ops.my_dict, {'a': 1, 'c': 3})

if __name__ == "__main__":
    unittest.main()
