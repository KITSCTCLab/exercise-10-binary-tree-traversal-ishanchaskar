class BinaryTreeNode:
    def __init__(self, data):
f binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
    # Write your code here


def inorder(root) -> None:
    # Write your code here


def preorder(root) -> None:
    # Write your code here


def postorder(root) -> None:
    # Write your code here


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
c
