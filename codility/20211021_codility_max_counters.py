# You are given N counters, initially set to 0, and you have two possible operations on them:

# increase(X) − counter X is increased by 1,
# max counter − all counters are set to the maximum value of any counter.
# A non-empty array A of M integers is given. This array represents consecutive operations:

# if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
# if A[K] = N + 1 then operation K is max counter.
# For example, given integer N = 5 and array A such that:

#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the values of the counters after each consecutive operation will be:

#     (0, 0, 1, 0, 0)
#     (0, 0, 1, 1, 0)
#     (0, 0, 1, 2, 0)
#     (2, 2, 2, 2, 2)
#     (3, 2, 2, 2, 2)
#     (3, 2, 2, 3, 2)
#     (3, 2, 2, 4, 2)
# The goal is to calculate the value of every counter after all operations.

# Write a function:

# def solution(N, A)

# that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

# Result array should be returned as an array of integers.

# For example, given:

#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the function should return [3, 2, 2, 4, 2], as explained above.

# Write an efficient algorithm for the following assumptions:

# N and M are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..N + 1].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    # brute force would be linear search and add counter to output list
    # iterate len(A) times
    # the size of the out is N
    # max counter is broadcasting max(out) to out
    # TC:O(N*M); M possibly from list comprehension

    if not A:
        return A

    out = [0 for i in range(N)]

    for n in A:
        if n > N:
            temp = max(out) #corrected for slight TC improvement
            out = [temp for i in range(N)]
        else:
            out[n-1] += 1

    return out

def solution(N, A):
    # search without explicit update of all item in the list
    # TC: O(N)

    if not A:
        return A

    out = [0 for i in range(N)]
    temp_max = 0
    curr_max = 0

    for n in A:
        if n > N:
            temp_max = curr_max #corrected so that max is only between two values in each iteration
        else:
            if out[n-1] < temp_max:
                out[n-1] = temp_max #update individually

            out[n-1] += 1
            curr_max = max(curr_max, out[n-1])

    for i in range(N):
        if out[i] < temp_max:
            out[i] = temp_max

    return out