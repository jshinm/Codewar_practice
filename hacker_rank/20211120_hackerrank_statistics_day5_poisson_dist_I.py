# Objective
# In this challenge, we learn about Poisson distributions.

# Task
# A random variable, X, follows Poisson distribution with mean of 2.5. 
# Find the probability with which the random variable X is equal to 5.

# Input Format
# The first line contains X's mean. The second line contains the value we want the probability for:

# Output Format
# Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e., 1.234 format).

# poisson is concerned with the average of events
# p(X) = lambda^k * e^-lambda / k!
# where lambda is the avg success, k is the actual success
# the question prompts that X is equal to 5

import sys
import math

param = []

for line in sys.stdin:
    tmp = line.replace('\n', '')
    param += list(map(float, tmp.split(' ')))

def pois(*param):
    l, k = param
    e = 2.71828
    p = l**k * e**-l / math.factorial(int(k))
    
    return round(p, 3)
    
print(pois(*param))