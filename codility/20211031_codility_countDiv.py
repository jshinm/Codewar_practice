# Write a function:

# def solution(A, B, K)

# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

# { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

# Write an efficient algorithm for the following assumptions:

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

def solution(A, B, K):
    # find the multiples of K within the range
    # 2 in [6, 11] => 3
    # 3, 5 => 5 - 3 + 1 = 3
    # find left and right limit
    # TC:O(2N)-> O(N)

    l = 0
    r = 0

    for i in range(A,B+1):
        if i%K == 0:
            l = int(i/K)
            break
        if i == B: #exit conditional
            return 0

    for j in range(B,i-1,-1):
        if j%K == 0:
            r = int(j/K)
            break

    return r-l+1