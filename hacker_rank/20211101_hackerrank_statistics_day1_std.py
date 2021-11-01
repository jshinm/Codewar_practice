# Objective
# In this challenge, we practice calculating standard deviation

# Task
# Given an array, arr, of n integers, calculate and print the standard deviation. 
# Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e.,12.3 format). 
# An error margin of +-0.1 will be tolerated for the standard deviation.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    pass

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
