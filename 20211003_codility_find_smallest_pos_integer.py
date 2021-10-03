# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Copyright 2009–2021 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # A is the list
    # sort(set(list))
    # iterate over numbers
    # TC: O(2N)

    A = [i for i in A if i > 0]
    newA = sorted(set(A))

    if len(newA) == 0 or min(newA) != 1:
        return 1

    for i, n in enumerate(newA):
        if i+1 != n:
            return i+1
    
    return len(newA)+1