
# 3 POSSIBILITIES:
    # 1/ NODE DELETED IS LEAF(NO CHILDREN)
    # 2/ NODE DELETED HAS 1 CHILD: copy the child to the node and delete the child
    # 3/ NODE DELETE HAS 2 CHILDREN: find indorder succesor of the node (when the right child not empty)-copy content and delete the inroder sucessor

# Python program to demonstrate delete operation
# in binary search tree

# A Binary Tree Node
class Node:
    # constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # inorder traversal of BST
def inorder(root):


