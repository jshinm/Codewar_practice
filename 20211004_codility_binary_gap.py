# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. 
# The number 20 has binary representation 10100 and contains one binary gap of length 1. 
# The number 15 has binary representation 1111 and has no binary gaps. 
# The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 
# and so its longest binary gap is of length 5. Given N = 32 
# the function should return 0, because N has binary representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    # 1. binary translation
    # 2. assess binary gaps
    
    #integer to binary conversion
    #divide by 2 until quotient is 0
    #the remainder in reverse order is binary for the integer
    #e.g. 12 => 1100
    #12 / 2 = 6 + 0
    #6 / 2  = 3 + 0
    #3 / 2  = 1 + 1
    #1 / 2  = 0 + 1

    ans = ''

    while True: #binarization
        temp = int(N % 2)
        N = N / 2
        ans += str(temp)

        if N < 1:
            break

    ans = ans[::-1] #reversing remainer order
    temp = 0
    max_num = 0

    if ans[0] == '0': #edge case
        return 0

    for i in ans: #O(N) search
        
        if i == '0': #if not closed by 1, then not applied to max_num
            temp += 1
        else:
            if max_num < temp:
                max_num = temp
            temp = 0

    return max_num