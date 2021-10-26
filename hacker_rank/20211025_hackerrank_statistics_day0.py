# Objective
# In this challenge, we practice calculating the mean, median, and mode. 

# Task
# Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. 
# If your array contains more than one modal value, choose the numerically smallest one.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

for line in sys.stdin:
    out = line.rstrip().split(' ')
    
out = sorted(list(map(int, out)))
N = len(out)

print(sum(out)/N) #mean

if N % 2 == 0:
    idx = [int(N/2-1), int(N/2)]
elif N % 2 == 1:
    idx = [int(N/2)]

num = [out[i] for i in idx]
print(sum(num)/len(num)) #median

dic = {}

for i in out:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

# the output list is already sorted, so sorted by freq once more will be enough
print(sorted(dic.items(), key=lambda x:x[1], reverse=True)[0][0]) #mode


# Objective
# In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean. 
# Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given an array, X, of N integers and an array, W, representing 
# the respective weights of X's elements, calculate and print the weighted mean of X's elements.
# Your answer should be rounded to a scale of 1 decimal place.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    out = [i * j for i, j in zip (X, W)]
    print (round(sum(out) / sum(W), 1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)