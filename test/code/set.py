class SetOperations:
    def __init__(self, my_set):
        self.my_set = my_set

    # Method to get the length of the set
    def get_length(self):
        return len(self.my_set)

    # Method to add a new element to the set
    def add_element(self, new_element):
        self.my_set.add(new_element)

    # Method to remove an element from the set
    def remove_element(self, element):
        if element in self.my_set:
            self.my_set.remove(element)

    # Method to check if a specified element is present in the set
    def element_in_set(self, element):
        return element in self.my_set

    # Method to get the union of two sets
    def union_sets(self, other_set):
        return self.my_set.union(other_set)

    # Method to get the intersection of two sets
    def intersection_sets(self, other_set):
        return self.my_set.intersection(other_set)

    # Method to get the difference between two sets
    def difference_sets(self, other_set):
        return self.my_set.difference(other_set)
