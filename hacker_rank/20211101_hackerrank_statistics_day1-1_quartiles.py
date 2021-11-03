# Objective
# In this challenge, we practice calculating quartiles.

# Task
# Given an array, arr, of n integers, calculate the respective first quartile (Q1), 
# second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def median(arr, N):
    
    if N % 2 == 0:
        idx = [int(N/2-1), int(N/2)]
    elif N % 2 == 1:
        idx = [int(N/2)]

    num = [arr[i] for i in idx]
    
    return sum(num)/len(num), idx
    

def quartiles(arr):
    # Write your code here
    arr = sorted(arr)
    Q2, idx = median(arr, len(arr))
    
    if len(idx) == 1:
        Q1, _ = median(arr[:idx[0]], len(arr[:idx[0]]))
        Q3, _ = median(arr[idx[0]+1:], len(arr[idx[0]+1:]))
    else:
        Q1, _ = median(arr[:idx[0]+1], len(arr[:idx[0]+1]))
        Q3, _ = median(arr[idx[1]:], len(arr[idx[1]:]))
    
    return list(map(int, [Q1,Q2,Q3]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()