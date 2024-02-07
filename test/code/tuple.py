class TupleOperations:
    def __init__(self, my_tuple):
        self.my_tuple = my_tuple

    # Method to get the length of the tuple
    def get_length(self):
        return len(self.my_tuple)

    # Method to concatenate two tuples
    def concatenate_tuples(self, other_tuple):
        return self.my_tuple + other_tuple

    # Method to count occurrences of a specified element in the tuple
    def count_element(self, element):
        return self.my_tuple.count(element)

    # Method to check if a specified element is present in the tuple
    def element_in_tuple(self, element):
        return element in self.my_tuple

    # Method to create a set from the tuple
    def convert_to_set(self):
        return set(self.my_tuple)


