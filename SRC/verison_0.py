# This version is the basic version.
# In case of equal data, it send to right


class NodeVersion0:

    def __init__(self, key):
        """Constructor to create a new node"""
        self.left = None
        self.right = None
        self.parent = None
        self.data = key

    def place_in_left(self, new_data, count):
        """Put the new node as a left-child"""
        if self.left:
            return self.left.insert(new_data, count)

        else:
            self.left = NodeVersion0(new_data)
            self.left.parent = self
            return count

    def place_in_right(self, new_data, count):
        """Put the new node as a right-child"""
        if self.right:
            return self.right.insert(new_data, count)

        else:
            self.right = NodeVersion0(new_data)
            self.right.parent = self
            return count

    def eq_data(self, new_data, count):
        """Put the new node as a right-child"""
        return self.place_in_right(new_data, count)

    def insert(self, new_data, count):
        """ Insert an element into the bst """
        if self.data == new_data:
            count += 1
            return self.eq_data(new_data, count)

        elif new_data < self.data:
            count += 1
            return self.place_in_left(new_data, count)

        else:
            count += 1
            return self.place_in_right(new_data, count)

    def min_value(self):
        """Get the minimum value"""
        current = self

        # loop down to find the lefmost leaf
        while current.left is not None:
            current = current.left

        return current

    @staticmethod
    def in_order_successor(node):
        """Find the successor node"""
        # Step 1 of the algorithm
        if node.right is not None:
            return node.right.min_value()

        # Step 2 of the algorithm
        node_parent = node.parent

        while node_parent is not None:
            if node != node_parent.right:
                break

            node = node_parent
            node_parent = node_parent.parent

        return node_parent

    def sort_tree(self):
        """Sorting the values from small to larger"""
        minimum_data = self.min_value()
        sort_tree = []

        while minimum_data is not None:
            sort_tree.append(minimum_data)
            minimum_data = self.in_order_successor(minimum_data)

        return sort_tree




