# In this version every node have list with the equal node

from verison_0 import NodeVersion0


class NodeVersionB(NodeVersion0):
    def __init__(self, key):
        """Constructor to create a new node"""
        super(NodeVersionB, self).__init__(key)
        self.elem = []

    def eq_data(self, new_data, count):
        """Put the new node in the head of the list"""
        self.elem.append(NodeVersionB(new_data))
        return count

    def sort_tree(self):
        """Sorting the values from small to larger"""
        minimum_data = self.min_value()
        sort_tree = []
        while minimum_data is not None:
            for item in minimum_data.elem:
                sort_tree.append(item)
            sort_tree.append(minimum_data)
            minimum_data = self.in_order_successor(minimum_data)
        return sort_tree

    def place_in_left(self, new_data, count):
        """put the new node as a left-child"""
        if self.left:
            return self.left.insert(new_data, count)
        else:
            self.left = NodeVersionB(new_data)
            self.left.parent = self
            return count

    def place_in_right(self, new_data, count):
        """put the new node as a right-child"""
        if self.right:
            return self.right.insert(new_data, count)
        else:
            self.right = NodeVersionB(new_data)
            self.right.parent = self
            return count
