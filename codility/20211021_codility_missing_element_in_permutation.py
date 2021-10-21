# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

# Your goal is to find that missing element.

# Write a function:

# def solution(A)

# that, given an array A, returns the value of the missing element.

# For example, given array A such that:

#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # iterate over the list with an increment of 1
    # return missing value

    if not A: #edge case for empty list
        return 1

    if len(A) < 2:
        return A[0]

    A.sort() #TC: O(n log n)

    for i, n in enumerate(A[:-1]):
        if n+1 != A[i+1]:
            return n+1

    if max(A) == len(A): #edge case for the last missing item
        return len(A)+1
    
    return 1 #edge case for the first missing