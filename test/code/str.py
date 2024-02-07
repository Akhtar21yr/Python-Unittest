class StringOperations:
    def __init__(self, string: str):
        self.string = string
    
    # Method to reverse the string
    def reverse_string(self):
        return self.string[::-1]

    # Method to convert the string to uppercase
    def upper_case(self):
        return self.string.upper()

    # Method to convert the string to lowercase
    def lower_case(self):
        return self.string.lower()

    # Method to center the string within a specified width, optionally filling with a given element
    def center_elements(self, num=4, ele=None):
        if ele:
            return self.string.center(num, ele)
        else:
            return self.string.center(num)

    # Method to count occurrences of a specified word in the string
    def count_str(self, word: str):
        return self.string.count(word)

    # Method to check if the string ends with a specified word
    def check_end_str(self, word: str):
        return self.string.endswith(word)

    # Method to check if the string starts with a specified word
    def check_start_str(self, word: str):
        return self.string.startswith(word)

    # Method to find the index of the first occurrence of a specified word in the string
    def find_str(self, word: str):
        return self.string.find(word)

    # Method to find the index of the first occurrence of a specified word in the string
    def index_str(self, word: str):
        return self.string.index(word)

    # Method to check if all characters in the string are alphabetic
    def check_alpha(self):
        return self.string.isalpha()

    # Method to check if all characters in the string are numeric
    def check_numeric(self):
        return self.string.isnumeric()

    # Method to replace occurrences of a specified word with another word
    def replace_str(self, word1, word2):
        return self.string.replace(word1, word2)

    # Method to split the string into a list of words using whitespace as the default separator
    def split_str(self):
        return self.string.split()

    # Method to create a list from the string, using a specified separator (default is space)
    def create_list(self, separator=' '):
        return self.string.split(separator)

    # Method to create a tuple from the string, using a specified separator (default is space)
    def create_tuple(self, separator=' '):
        return tuple(self.string.split(separator))

    # Method to create a set from the string, using a specified separator (default is space)
    def create_set(self, separator=' '):
        return set(self.string.split(separator))
