# Write a function

# def solution(A)

# that, given an array A consisting of N integers, returns the number of distinct values in array A.

# For example, given array A consisting of six elements such that:

#  A[0] = 2    A[1] = 1    A[2] = 1
#  A[3] = 2    A[4] = 3    A[5] = 1
# the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # input is a list
    # simple solution
    return len(set(A))

def solution(A):
    # write your code in Python 3.6
    # input is a list
    # manual solution
    # TC: O(N**2) worst
    chk = []

    for i in A:
        if i not in chk:
            chk.append(i)

    return len(chk)

def solution(A):
    # write your code in Python 3.6
    # hashmap method
    # TC: O(N) much faster than searching through the list
    chk = {}

    for i in A:
        if i not in chk:
            chk[i] = 0
    
    return len(chk.keys())