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