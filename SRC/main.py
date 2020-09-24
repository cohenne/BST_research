# the main of the project

import numpy
from BST import BST

if __name__ == '__main__':

    # Creates the BST
    bst_0 = BST("0")
    bst_a = BST("a")
    bst_b = BST("b")
    bst_c = BST("c")

    print("""This is a "mini-research" project on Binary Search Tree.
    We will look into several solutions to the key-repetitions issue\n""")
    
    n = int(input("Please enter n <array size>: "))

    version_type = input("""\n Please choose:
    a - for random number, \tb - to give your own numbers: """)

    input_arr = []

    while version_type != 'a' and version_type != 'b':
        version_type = input("Invalid input, please enter again ")

    # Select the type of insertion value
    if version_type == 'a':
        r = int(input("please enter r <range [0...r-1]>: "))
        input_arr = numpy.random.randint(0, r-1, n)
        print("\nThe elements are: ", end="")
        print(input_arr)

    elif version_type == 'b':
        print("please enter " + str(n) + " numbers, delimited by spaces:", end=' ')
        string = input()
        arr = string.split()

        if len(arr) > n:
            print("Only the " + str(n) + "S")

        for i in range(0, n):
            input_arr.append(int(arr[i]))

    for i in input_arr:
        bst_0.insert(i)
        bst_a.insert(i)
        bst_b.insert(i)
        bst_c.insert(i)

    # Print the sorted values and the number of comparisons
    bst_0.print_sort_tree()

    print("""\nNumber of comparisons for building the tree:
    Strategy:  0\t\ta\t\tb\t\tc
    ------------------------------------------------------
               """, end='')

    bst_0.print_count()
    bst_a.print_count()
    bst_b.print_count()
    bst_c.print_count()


