class ListOperations:
    def __init__(self, my_list):
        self.my_list = my_list

    # Method to get the sum of all elements in the list
    def get_sum(self):
        return sum(self.my_list)

    # Method to get the average of all elements in the list
    def get_average(self):
        if not self.my_list:
            return None
        return sum(self.my_list) / len(self.my_list)

    # Method to get the minimum value in the list
    def get_min_value(self):
        if not self.my_list:
            return None
        return min(self.my_list)

    # Method to get the maximum value in the list
    def get_max_value(self):
        if not self.my_list:
            return None
        return max(self.my_list)

    # Method to sort the list in ascending order
    def sort_list(self):
        return sorted(self.my_list)

    # Method to reverse the order of elements in the list
    def reverse_list(self):
        return list(reversed(self.my_list))

    # Method to remove duplicates from the list
    def remove_duplicates(self):
        return list(set(self.my_list))

    # Method to check if a specified element is present in the list
    def element_in_list(self, element):
        return element in self.my_list

    # Method to count occurrences of a specified element in the list
    def count_element(self, element):
        return self.my_list.count(element)

    # Method to add a new element to the end of the list
    def add_element(self, new_element):
        self.my_list.append(new_element)

    # Method to remove the first occurrence of a specified element from the list
    def remove_element(self, element):
        if element in self.my_list:
            self.my_list.remove(element)
