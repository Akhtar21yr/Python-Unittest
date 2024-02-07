import unittest
from code.str import StringOperations

class TestStringOperations(unittest.TestCase):
    def setUp(self):
        # Initialize a test string
        self.test_string = "Hello, World!"
        # Create an instance of StringOperations with the test string
        self.string_ops = StringOperations(self.test_string)

    # Method to test reversing the string
    def test_reverse_string(self):
        self.assertEqual(self.string_ops.reverse_string(), "!dlroW ,olleH")

    # Method to test converting the string to uppercase
    def test_upper_case(self):
        self.assertEqual(self.string_ops.upper_case(), "HELLO, WORLD!")

    # Method to test converting the string to lowercase
    def test_lower_case(self):
        self.assertEqual(self.string_ops.lower_case(), "hello, world!")

    # Method to test centering the string within a specified width, optionally filling with a given element
    def test_center_elements(self):
        self.assertEqual(self.string_ops.center_elements(20, '*'), "***Hello, World!****")

    # Method to test counting occurrences of a specified word in the string
    def test_count_str(self):
        self.assertEqual(self.string_ops.count_str('l'), 3)

    # Method to test checking if the string ends with a specified word
    def test_check_end_str(self):
        self.assertTrue(self.string_ops.check_end_str('World!'))

    # Method to test checking if the string starts with a specified word
    def test_check_start_str(self):
        self.assertTrue(self.string_ops.check_start_str('Hello'))

    # Method to test finding the index of the first occurrence of a specified word in the string
    def test_find_str(self):
        self.assertEqual(self.string_ops.find_str('World'), 7)

    # Method to test finding the index of the first occurrence of a specified word in the string
    def test_index_str(self):
        self.assertEqual(self.string_ops.index_str('World'), 7)

    # Method to test checking if all characters in the string are alphabetic
    def test_check_alpha(self):
        self.assertFalse(self.string_ops.check_alpha())

    # Method to test checking if all characters in the string are numeric
    def test_check_numeric(self):
        self.assertFalse(self.string_ops.check_numeric())

    # Method to test replacing occurrences of a specified word with another word
    def test_replace_str(self):
        self.assertEqual(self.string_ops.replace_str('Hello', 'Hi'), "Hi, World!")

    # Method to test splitting the string into a list of words using whitespace as the default separator
    def test_split_str(self):
        self.assertEqual(self.string_ops.split_str(), ['Hello,', 'World!'])

    # Method to test creating a list from the string, using a specified separator (default is space)
    def test_create_list(self):
        self.assertEqual(self.string_ops.create_list(), ['Hello,', 'World!'])

    # Method to test creating a tuple from the string, using a specified separator (default is space)
    def test_create_tuple(self):
        self.assertEqual(self.string_ops.create_tuple(), ('Hello,', 'World!'))

    # Method to test creating a set from the string, using a specified separator (default is space)
    def test_create_set(self):
        self.assertEqual(self.string_ops.create_set(), {'Hello,', 'World!'})


if __name__ == '__main__':
    unittest.main()
