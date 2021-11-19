# Objective
# In this challenge, we go further with geometric distributions.

# Task
# The probability that a machine produces a defective product is 1/3. 
# What is the probability that the 1st defect is found during the first 5 inspections?

# Input Format
# The first line contains the respective space-separated numerator and denominator 
# for the probability of a defect, and the second line contains the inspection 
# we want the probability of the first defect being discovered by:

# Output Format
# Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e., 1.234 format).

# first defect found DURING the first 5 inspections
# p(within 5 trials) = p(1st) + p(2nd) + p(3rd) + p(4th) + p(5th)

import sys

param = []

for line in sys.stdin:
    tmp = line.replace('\n', '')
    param += list(map(float,tmp.split(' ')))

def geo(n,p):
    q = 1-p
    prob = 0
    
    for i in range(1,int(n+1)):
        prob += q**(i-1)*p
        
    return round(prob,3)

print(geo(n=param[2],p=param[0]/param[1]))