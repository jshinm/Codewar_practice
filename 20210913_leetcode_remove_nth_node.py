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
    def removeNthFromEnd_I(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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

    def removeNthFromEnd_II(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #recursive method - removing a target node
        def remove(node):

            if node == None:
                return 0, node

            i, node.next = remove(node.next) #assigning node.next to node.next (n+1 to n+1)
            return i+1, (node, node.next)[i+1 == n] #conditional return at nth node assigning 
                                                    #node.next to node.next.next (n+2 to n+1) 

        return remove(head)[1] #returning the class

    def removeNthFromEnd_III(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two pointer method
        fast = slow = head #initialize two pointers

        if head.next == None: #edge case when 1 or 0 lenth is passed
            return head.next

        for _ in range(n): #move forward pointer n steps away from the behind pointer
            fast = fast.next

        if fast == None: #for edge case when length is 2 and n is 1
            return head.next #simply return the second item in the list

        while (fast.next != None): #move two pointers until the forward reaches the end
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next #move n+1th node to nth node

        return head #returns manipulated object by two pointers

#testing pointer concept in python
class Test:
    def __init__(self):
        self.value = 0

#objects assigned to a value is working as a pointer
tester = Test()
pointer1 = pointer2 = tester
pointer1.value = 2
print(tester.value)

#value assigned to a value creates another value of the same value
i = 2
pa = pb = i
pa = 3
print(i)