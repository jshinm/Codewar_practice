# Objective
# In this challenge, we practice calculating the interquartile range.

# Task
# The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3-Q1).

# Given an array, arr, of n integers and an array, freqs, representing the respective frequencies of 
# values's elements, construct a data set, S, where each values[i] occurs at frequency freqs[i]. 
# Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).

# Tip: Be careful to not use integer division when averaging the middle two elements 
# for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
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

    return [Q1,Q2,Q3]

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    # expand values according to freqs
    # compute IQR based on expanded values

    all_val = []

    for i, n in enumerate(freqs):
        all_val += [values[i]]*n

    quart = quartiles(all_val)

    print (round(quart[2]-quart[0],1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)