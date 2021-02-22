"""
@   Loop Detection | 2.8

@   Problem
    Given a circular linked list, implement an algorithm that returns the node 
    at the beginning of the loop (cycle).

@   Example
    Input:      [A] -> [B] -> [C] -> [D] -> [E] -> [C (Same as before)] -> Null

    Output:     C

@   Template:
    01. We create a dictionary of seen_nodes
    02. Comparate new nodes with seen_nodes
    

@   Explanation:
    https://github.com/w-hat/ctci-solutions/blob/master/ch-02-linked-lists/08-loop-detection.py

"""

# Given:
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


# Approach 01: Hash Table
def loopNode(self, head):
    seen_nodes = {}

    while head is not None:
        if head in seen_nodes:
            return head
        seen_nodes[head] = True
        head = head.next
    return None