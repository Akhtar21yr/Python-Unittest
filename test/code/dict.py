class DictionaryOperations:
    def __init__(self, my_dict):
        self.my_dict = my_dict

    # Method to get the keys of the dictionary
    def get_keys(self):
        return list(self.my_dict.keys())

    # Method to get the values of the dictionary
    def get_values(self):
        return list(self.my_dict.values())

    # Method to check if a specified key is present in the dictionary
    def key_in_dict(self, key):
        return key in self.my_dict

    # Method to check if a specified value is present in the dictionary
    def value_in_dict(self, value):
        return value in self.my_dict.values()

    # Method to add a new key-value pair to the dictionary
    def add_key_value(self, key, value):
        self.my_dict[key] = value

    # Method to remove a key-value pair from the dictionary
    def remove_key_value(self, key):
        if key in self.my_dict:
            del self.my_dict[key]


