# In this version, in the case of an equal,
# turn left or right according to the value in "dir"

from verison_0 import NodeVersion0


class NodeVersionA(NodeVersion0):

    def __init__(self, key):
        """Constructor to create a new node"""
        super(NodeVersionA, self).__init__(key)
        self.dir = "LEFT"

    def eq_data(self, new_data, count):
        """Put the new node by the value in "'dir'"""
        if self.dir == "LEFT":
            self.dir = "RIGHT"
            return self.place_in_left(new_data, count)
        else:
            self.dir = "LEFT"
            return self.place_in_right(new_data, count)

    def place_in_left(self, new_data, count):
        """Put the new node as a left-child"""
        if self.left:
            return self.left.insert(new_data, count)
        else:
            self.left = NodeVersionA(new_data)
            self.left.parent = self
            return count

    def place_in_right(self, new_data, count):
        """Put the new node as a right-child"""
        if self.right:
            return self.right.insert(new_data, count)
        else:
            self.right = NodeVersionA(new_data)
            self.right.parent = self
            return count
