# A non-empty array A consisting of N integers is given.

# A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

# The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

# For example, array A such that:

#     A[0] = 3
#     A[1] = 2
#     A[2] = 6
#     A[3] = -1
#     A[4] = 4
#     A[5] = 5
#     A[6] = -1
#     A[7] = 2
# contains the following example double slices:

# double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
# double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
# double slice (3, 4, 5), sum is 0.
# The goal is to find the maximal sum of any double slice.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

# For example, given:

#     A[0] = 3
#     A[1] = 2
#     A[2] = 6
#     A[3] = -1
#     A[4] = 4
#     A[5] = 5
#     A[6] = -1
#     A[7] = 2
# the function should return 17, because no double slice of array A has a sum of greater than 17.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [3..100,000];
# each element of array A is an integer within the range [−10,000..10,000].

def solution(A):
    # write your code in Python 3.6
    # find the best sequence [i:j] up to N-2th index
    # N-2 for divider, N-1 for the item, N as not counted according to the statement
    # find the best subsequent sequence [j+1:N-1]
    
    # but the divider must be considered in the process
    # such that two of either left or right side to the divider should be chosen
    # after which best sum is chosen
    # left first then right => A[1:-2] then A[maxi+2:-1]
    # right first then left => A[2:-1] then A[1:maxi]
    # compute the max of these two scenarios

    # alternative case involves getting the max sequence from A[1:-1]
    # take out the min val as a divider

    # alternatively take only the positive number on the left and max on the right
    # this doesn't work with simple [1,2,3,4,5]

    # the previous code only scores 50%

    # the max on the left may not yield the max of both left and right combined
    # thus all possible combination should be acquired
    # TC:O(2N)

    #zero is to account for the dividier between lmax and rmax 
    lmax = [0]
    rmax = [0]
    tmax = []

    cmax = 0 #initialize current max

    for i, n in enumerate(A[1:-2]):
        cmax = max(0, cmax+n)
        lmax.append(max(0, cmax))

    cmax = 0

    for i, n in enumerate(A[len(A)-2:1:-1]):
        cmax = max(0, cmax+n)
        rmax.append(max(0, cmax))

    for n, m in zip(lmax, rmax[::-1]):
        tmax.append(max(0, n+m))

    return max(tmax)

    # previous code
def solution(A):
    out = []

    if len(A) < 4:
        return 0

    tmax = cmax = A[1]
    maxarr = carr = [A[1]]

    for n in A[2:-1]:
        if cmax+n >= n:
            cmax += n
            carr.append(n)
        else:
            cmax = n
            carr = []

        if cmax > tmax:
            tmax = cmax
            maxarr = carr.copy()

    out = [sum(maxarr) - min(maxarr)]

    tmax = cmax = A[1]
    maxi = 1

    for i, n in enumerate(A[2:-2]):
        cmax = max(n+cmax, n)
        if tmax != max(cmax, tmax):
            tmax = max(cmax, tmax)
            maxi = i+2

    if not A[maxi+2:-1]:
        vmax = 0
    else:
        cmax = A[maxi+2]
        vmax = A[maxi+2]

        for m in A[maxi+3:-1]:
            cmax = max(m+cmax, m)
            vmax = max(cmax, vmax)

    out.append(tmax + vmax)

    tmax = cmax = A[2]
    maxi = tmpi = 2

    for i, n in enumerate(A[3:-1]):
        if n+cmax >= n:
            cmax = n+cmax
        else:
            cmax = n
            tmpi = i+3

        if tmax != max(cmax, tmax):
            tmax = max(cmax, tmax)
            maxi = tmpi

    if not A[1:maxi-1]:
        vmax = 0
    else:
        cmax = A[1]
        vmax = A[1]

        for m in A[2:maxi-1]:
            cmax = max(m+cmax, m)
            vmax = max(cmax, vmax)

    out.append(tmax + vmax)

    return max(out)