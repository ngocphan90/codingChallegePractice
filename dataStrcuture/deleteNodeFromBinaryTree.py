
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
    if root is not None:
        inorder(root.left)
        print(root.key),
        inorder(root.right)
#insert a new node with given key
def insert(node,key)
    #if the tree is empty, return a new node
    if node is None:
        return Node(key)
    #otherwise recur down to the tree
    if key< node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right,key)
    #return the unchanged node pointer
    return node

# minimum key value found in  that tree , noted the entire tree not need to be searched
def minValue(node):
    current = node
    #loop down to find the most leaf
    while(current.left is not None):
        current = current.left
    return current

#delete the key and return the new root
def deleteNode (root,key):
    # Base case
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif (key > root.key):
        root.right = deleteNode(root.right, key)

    # if key is same as root key then this is the node to be deleted
    else:
        # Node with only 1 child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with 2 children
        # get the inorder successor (smallest in the right subtree)
        temp = minValue(root.right)
        # copy the inorder successor's content to this node
        root.key = temp.key
        #delete inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root

# Driver code
"""         50 
        /        \ 
        30        70
      /    \    /    \
     20     40  60    80 """

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)








