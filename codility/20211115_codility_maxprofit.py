# An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

# For example, consider the following array A consisting of six elements such that:

#   A[0] = 23171
#   A[1] = 21011
#   A[2] = 21123
#   A[3] = 21366
#   A[4] = 21013
#   A[5] = 21367
# If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

# Write a function,

# def solution(A)

# that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

# For example, given array A consisting of six elements such that:

#   A[0] = 23171
#   A[1] = 21011
#   A[2] = 21123
#   A[3] = 21366
#   A[4] = 21013
#   A[5] = 21367
# the function should return 356, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..400,000];
# each element of array A is an integer within the range [0..200,000].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # brute force would be to run two loops and check for every combination
    # TC: O(n^2)

    maxval = None

    for i, n in enumerate(A[:-1]):
        for m in A[i+1:]:
            if not maxval or maxval < m-n:
                maxval = m-n
                
    if not maxval:
        return 0
    
    if maxval < 0:
        return 0

    return maxval

def solution(A):
    # write your code in Python 3.6
    # sweep once and find max and min
    # if max_i > min_i, this is maximal loss
    # thus must find max that occurs later than min occurring

    # find min, max in a single pass
    # if min_i > min_i+1, update min, compute diff
    # if min_i < min_i+1 and max_i > max_i+1, update max
    # TC:O(N)

    if len(A) < 2:
        return 0

    out = [] #list of difference
    dic = {'max': None, 'min': A[0]}

    for i, n in enumerate(A[1:]):
        if dic['min'] > n:
            if dic['max']:
                out.append(dic['max'] - dic['min'])
            dic['min'] = n
            dic['max'] = None
        elif dic['min'] < n:
            if dic['max']:
                if dic['max'] < n:
                    dic['max'] = n
            else:
                dic['max'] = n

    if dic['max'] != None:
        out.append(dic['max'] - dic['min'])

    if not out:
        return 0

    out = max(out)

    if out < 0:
        return 0
    else:
        return out