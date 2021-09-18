# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: l1 = [], l2 = []
# Output: []
# Example 3:

# Input: l1 = [], l2 = [0]
# Output: [0]

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #recursive method
        #TC:O(N)
        temp = []

        while l1:
            temp.append(l1.val)
            l1 = l1.next

        while l2:
            temp.append(l2.val)
            l2 = l2.next

        temp.sort(reverse=True) #reversed order since lst is popped from the end

        def create_node(lst):
            if lst != []:
                return ListNode(val=lst.pop(), next=create_node(lst))
            else:
                return None

        return create_node(temp)