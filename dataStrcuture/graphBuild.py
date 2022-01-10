# Edge List: list of array of all edge in the graph
# index of the array us the value of actual graph node
# const graph = [[0,2],[2,3],...]

# adjacent list: an array consisting of address of linkedlist( weighted graph)
# const graph = we can use array, object or linkedlist [[2],[2,3],[0,1,3],[1,2]]

# adjacent matrix: is a 2Dimensional  array (weighted graph)
# const graph = 0 mean no and 1 mean yes  to see if node has connection
#    [
#        [0,0,1,0],  # index of 0  connected to 2
#        [0,0,1,1],  # node 1 connected to 2,3
#        [1,1,0,1],....
#        [0,1,1,0] ....
#    ]
# if it is object

#    {
#        0:[0, 0, 1, 0],  # index of 0  connected to 2
#        1: [0, 0, 1, 1],  # node 1 connected to 2,3
#        2: [1, 1, 0, 1], ....
#        3: [0, 1, 1, 0]....
#    }



