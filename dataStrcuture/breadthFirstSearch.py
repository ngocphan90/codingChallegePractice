# program print out visited node of bread first search

# current node = root
# list = [] : result
# queue = []: keep track of all the visited node

# add to the queue the root item
# queue.append(current node)
# while queue > 0{
    # currentNode = queue.pop(0)
    # list.append(currentNode.value)
    # if currentNode.left:
        # queue.append(currentNode.left)
    # if currentNode.right:
        # queue.append(currentNode.right)
# return list


# recurisive BFS

# breadFirstSearch(queue, list)
# if !queue.length:
    # return list

# currentNode = queue.pop(0)
# list.append(currentNode.value)

#   if currentNode.left:
# queue.append(currentNode.left)
#   if currentNode.right:
# queue.append(currentNode.right)

# return breadFirstSearch(queue, list)

# function call breadFirstSearch(this.root, [])


# DFSInorder()
    # return traverseInorder(root,[])

# traverseInorder(node, list)
# if (node.left)
#   traverseInorder(node.left, data)
# list.append(node.value)

# if (node.right)
#   traverseInorder(node.right, data)

# return list


# DFSPreOrder()
    # return traversePreorder(root,[])

# traversePreorder(node, list)
# list.append(node.value)
# if (node.left)
#   traverseInorder(node.left, data)


# if (node.right)
#   traverseInorder(node.right, data)

# return list



# DFSPostOrder()
    # return traversePostOrder(root,[])

# traversePostOrder(node, list)
# if (node.left)
#   traversePostOrder(node.left, data)

# if (node.right)
#   traversePostOrder(node.right, data)
# list.append(node.value)

# return list