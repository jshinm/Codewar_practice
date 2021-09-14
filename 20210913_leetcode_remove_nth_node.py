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