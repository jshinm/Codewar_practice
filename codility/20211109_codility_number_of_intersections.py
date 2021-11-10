# We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

# We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

# The figure below shows discs drawn for N = 6 and A as follows:

#   A[0] = 1
#   A[1] = 5
#   A[2] = 2
#   A[3] = 1
#   A[4] = 4
#   A[5] = 0


# There are eleven (unordered) pairs of discs that intersect, namely:

# discs 1 and 4 intersect, and both intersect with all the other discs;
# disc 2 also intersects with discs 0 and 3.
# Write a function:

# def solution(A)

# that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

# Given array A shown above, the function should return 11, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..2,147,483,647].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# unordered pair
# return -1 if # of intersection exceeds 10**7
# A[J] = (J - A[J], J + A[J]); suggests range
# count if two ranges fall within wihtout counting their duplicates
# example cases (11 cases)
# 0-1, 0-2, 0-4
# 1-2, 1-3, 1-4, 1-5
# 2-3, 2-4
# 3-4
# 4-5

def solution(A):
    # write your code in Python 3.6
    # brute force method (TLE)
    rng = []
    cnt = 0

    for i, n in enumerate(A): #TC: O(N)
        rng.append((i-n, i+n))

    rng.sort(key=lambda x: x[0]) #TC: O(N log N)

    for i, r in enumerate(rng[:-1]): #TC: O(N^2)
        for j, s in enumerate(rng[i+1:]):
            if cnt >= 10**7:
                return -1
            
            if r[1] >= s[0]:
                cnt += 1

    return cnt

def solution(A):
    # write your code in Python 3.6
    # alternative method
    # a circle has left and right limit for both of which act as a pair
    # we can count each circle based on that using two pointers
    l = []
    r = []
    # preset to 1 since actual addition occurs only after the second circle
    lp = 1 
    rp = 0
    # thus the current_overlap starts from 1 as well
    current_overlap = 1 
    cnt = 0

    for i, n in enumerate(A): #TC: O(N)
        l.append(i-n)
        r.append(i+n)

    # TC: O(N log N)
    l.sort() 
    r.sort()

    while lp < len(l):

        # edge case
        if cnt >= 10**7: 
            return -1

        # touching is also considered as an overlap as per problem
        if r[rp] >= l[lp]:
            cnt += current_overlap
            current_overlap += 1
            lp += 1
        else:
            current_overlap -= 1
            rp += 1

    return cnt