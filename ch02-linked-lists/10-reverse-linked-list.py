"""
@   Reverse a Linked List | 2.9

@   Problem
    Write code to remove duplicates from an unsorted linked list.

@   Example
    Input:      linked_list = [1,2,3,4,5,Null]
                [1] -> [2] -> [3] -> [4] -> [5] -> Null

    Output:     linked_list = [5,4,3,2,1,Null]
                Null <- [1] <- [2] <- [3] <- [4] <- [5]

@   Template:

    We dont change any the nodes itself     (self, x)
    We dont change the values               self.va = x
    We only have to change the pointers     self.next = None

    01. We have to iterate for each node of the linked list, making each node 
        (.next pointer) to point backwards (to the previous node we where on).
    02. We can't travel backwards in a Linked List, so we have to create a 
        variable to hold the previous value.
    03. Out first value will be the last, so we have to start our linked list
        as a Null (None)

@   Explanation:
    https://www.youtube.com/watch?v=XDO6I8jxHtA&t=9s

"""

# Given:
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


def reverseLinkedList(self, head):
    prev = None                 # We set the previous value [...]
    while head:                 # We write pur while loop [...]
        temp = head             # We set the temporary variable to hold the current value of head [...]
        head = head.next        # We iterate foward [...]
        temp.next = prev        # We change the pointer to the original node [...]
        prev = temp             # We change previous to the original node for next iteration [...]
    return prev                 # We return prev at the end of our loop [...]
