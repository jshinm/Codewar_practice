# You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

# The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

# Write a function:

# def solution(H)

# that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

# For example, given array H containing N = 9 integers:

#   H[0] = 8    H[1] = 8    H[2] = 5
#   H[3] = 7    H[4] = 9    H[5] = 8
#   H[6] = 7    H[7] = 4    H[8] = 8
# the function should return 7. The figure shows one possible arrangement of seven blocks.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array H is an integer within the range [1..1,000,000,000].

def solution(A):
    # write your code in Python 3.6
    # the only encounter case is if B[N] > B[N+1]
    # one fish gets eaten unless they are of same size
    # pop list until encounter condition is met
    # worst TC:O(2N)

    i0 = 0
    i1 = 1

    while (i0 != len(A)-1):
        if B[i0] > B[i1]:
            if A[i0] > A[i1]: #remove i1 and continue
                A.pop(i1) #splicing is much slower than pop method
                B.pop(i1)
            elif A[i0] < A[i1]: #remove i0 and backtrack once
                A.pop(i0) #pop(0) would yield TC:O(N)
                B.pop(i0) #in which case it's faster if reversed
                i0 -= 1   #collections deque is advised
                i1 -= 1
            else: #no removal and continue
                i0 += 1
                i1 += 1
        else: #continue
            i0 += 1
            i1 += 1
    return len(A)