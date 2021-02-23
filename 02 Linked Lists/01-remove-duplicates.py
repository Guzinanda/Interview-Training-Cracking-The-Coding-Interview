"""
@   Is Unique | 2.1

@   Problem
    Write code to remove duplicates from an unsorted linked list.

@   Example
    Input:      [1] -> [2] -> [2] -> [3] -> [4] -> [4] -> [5] -> Null

    Output:     [1] -> [2] -> [3] -> [4] -> [5] -> Null

@   Template:
    01.
    

@   Explanation:
    https://leetcode.com/problems/remove-duplicates-from-sorted-list/

"""

# Given:
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


def removeDuplicates(self, head):

    cur = head

    while cur and cur.next:               # We iterate while we have a value and somethign cur.next [...]
        if cur.val == cur.next.val:       # We set a conditional: If out cur is == to the next, then
            cur.next = cur.next.next      # our pointer will point to the .next.next pointer [...]
        else:                             # Else: If our cur is not == to the next, then
            cur = cur.next                # our pointer will continuing pointing to the .next [...]
    return head                           # We return the head [...]
