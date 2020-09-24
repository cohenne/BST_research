from verison_0 import node_version_0
from version_a import node_version_a
from verison_b import node_version_b
from version_c import node_version_c


class BST:
    def __init__(self, kind):
        """Constructor to create a new BST"""
        self.root = None
        self.count = 0
        self.kind = kind
        self.sort_tree = []

    def insert(self, d):
        """Adds value to the root"""
        if self.root:
            self.count = self.root.insert(d, self.count)
        elif self.kind == "0":
            self.root = node_version_0(d)
        elif self.kind == "a":
            self.root = node_version_a(d)
        elif self.kind == "b":
            self.root = node_version_b(d)
        elif self.kind == "c":
            self.root = node_version_c(d)

    def print_sort_tree(self):
        """Prints the sorted tree"""
        self.sort_tree = self.root.sort_tree()
        print("the sort sequence is: ", end='')
        for item in self.sort_tree:
            print(item.data, end=' ')

    def print_count(self):
        """Prints the number of comparisons"""
        print(self.count, end='\t\t')



