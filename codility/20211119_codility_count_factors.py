# A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

# For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the number of its factors.

# For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # find symmetric divisor sqrt(N)
    # TC: O(sqrt(N))
    cnt = 0
    sqrtN = N**(1/2)

    for i in range(1, int(sqrtN)+1):
        if N % i == 0:
            if i < sqrtN:
                cnt += 2
            else:
                cnt += 1

    return cnt

def solution(N):
    # write your code in Python 3.6
    # multiples of 2,3,5 + 1 and number itself
    # kind of brute force stytle
    # TC: O(N/2)
    out = [1, N]
    prime = []

    for i in [2,3,5]:
        if N % i == 0:
            prime.append(i)

    for i in prime:
        for j in range(i, N, i):
            if N % j == 0:
                out.append(j)

    return len(set(out))