# Objective
# In this challenge, we learn about geometric distributions.

# Task
# The probability that a machine produces a defective product is 1/3. 
# What is the probability that the 1st defect occurs the 5st item produced?

# Input Format
# The first line contains the respective space-separated numerator 
# and denominator for the probability of a defect, and the second 
# line contains the inspection we want the probability of being the first defect for:

# Output Format
# Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e., 1.234 format).

# prob of defective product: 1/3, p=1/3
# prob of normal product: 2/3, q=2/3
# 1st p at the 5th => geometric distribution
# g(n,p) = q^(n-1)*p = 1/3^(5-1)*(2/3)

import sys

param = []

for line in sys.stdin:
    tmp = line.replace('\n', '')
    param += list(map(float,tmp.split(' ')))

def geo(n,p):
    q = 1-p
    return round(q**(n-1)*p,3)

print(geo(n=param[2],p=param[0]/param[1]))