# The below function take head of Linked List as
# input and return Address of first node in
# the loop if present else return NULL.

''' Definition for singly-linked list.
* class ListNode:
*	 def __init__(self, x):
*		 self.val=x
*		 self.next=None
def newNode(key):

    temp = Node(key)
    return temp

*'''

def detectCycle(A):
    # Declaring map to store node
    # address
    uset = set()

    ptr = A

    # Default consider that no cycle
    # is present
    while (ptr != None):

        # Checking if address is already
        # present in map
        if (ptr in uset):
            return ptr

        # If address not present then
        # insert into the set
        else:
            uset.add(ptr)

        ptr = ptr.next

    return None


