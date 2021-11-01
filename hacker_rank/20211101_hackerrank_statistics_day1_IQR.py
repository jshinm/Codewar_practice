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

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    pass

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
