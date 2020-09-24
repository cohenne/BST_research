import random
from verison_0 import NodeVersion0


class NodeVersionC(NodeVersion0):

    def __init__(self, key):
        """Constructor to create a new node"""
        super(NodeVersionC, self).__init__(key)

    def eq_data(self, new_data, count):
        """Put the new node as left-child or right-child"""
        rand = random.randint(0, 1)

        if rand == 1:
            return self.place_in_left(new_data, count)

        else:
            return self.place_in_right(new_data, count)

    def place_in_left(self, new_data, count):
        """Put the new node as a left-child"""
        if self.left:
            return self.left.insert(new_data, count)

        else:
            self.left = NodeVersionC(new_data)
            self.left.parent = self
            return count

    def place_in_right(self, new_data, count):
        """Put the new node as a right-child"""
        if self.right:
            return self.right.insert(new_data, count)

        else:
            self.right = NodeVersionC(new_data)
            self.right.parent = self
            return count
