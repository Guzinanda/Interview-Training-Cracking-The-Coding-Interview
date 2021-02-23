"""
@   Loop Detection | 2.8

@   Problem
    Given a circular linked list, implement an algorithm that returns if the
    Linked List has a cyclce in it.

@   Example
    Input:      [A] -> [B] -> [C] -> [D] -> [E] -> [C (Same as before)] -> Null

    Output:     True

@   Template:
    Approach 01: Hash Table
    Approach 02: Floyd's Cycle Finding Algorithm

@   Explanation:
    https://leetcode.com/problems/linked-list-cycle/

"""

# Given:
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


# Approach 01: Hash Table
def hasCycle(self, head):
    seen_nodes = set()

    while head is not None:
        if head in seen_nodes:
            return True
        seen_nodes.add(head)
        head = head.next
    return False


# Approach 02: Floyd's Cycle Finding Algorithm
def hasFloydCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    
    except:
        return False
        