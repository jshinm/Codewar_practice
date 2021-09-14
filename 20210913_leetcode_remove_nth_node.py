# Given the head of a linked list, remove the nth node from the end of the list and return its head.

#recursion practice
def sum(n):
    if n != 0:
        return n + sum(n-1)

    return 0

print(sum(4)) #returns 10

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2) #nth number is n-1th number + n-2th number, both of which can be found recursively

print(fibonacci(5)) #0 1 1 2 3

def subsequent_add(n):
    if n == 0:
        return 0 + 1
    return subsequent_add(n-1) + 1 # func(0)[which returns 0 + 1] + 1 + 1 + 1 + 1 + 1, each +1 comes from each recursion

print(subsequent_add(5))

def addnum_lst(n):
    #embed 0 within n dimension list
    if n == 0:
        return 0
    return [addnum_lst(n-1)]

print(addnum_lst(5))

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #recursive method - shifting value
        def search(node):
            if node == None: #the last node index is 0
                return 0

            i = search(node.next) + 1 #index starts from 1
            # func(n) dissolved into first condtional which returns 0 at the end
            # sequence obtained from adding 1 into i when returning

            if i > n: 
                node.next.val = node.val #shifting nth val into n+1th val, thus the first val is a duplicate

            return i

        search(head)

        return head.next #the first val duplicate is removed