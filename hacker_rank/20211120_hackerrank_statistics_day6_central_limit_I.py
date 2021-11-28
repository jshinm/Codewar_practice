# Objective
# In this challenge, we practice solving problems based on the Central Limit Theorem.

# Task
# A large elevator can transport a maximum of 9800 pounds. 
# Suppose a load of cargo containing 49 boxes must be transported via the elevator.
# The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a standard deviation of 15 pounds. 
# Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

# The first line contains the maximum weight the elevator can transport. 
# The second line contains the number of boxes in the cargo. 
# The third line contains the mean weight of a cargo box, 
# and the fourth line contains its standard deviation.

# Output Format
# Print the probability that the elevator can successfully transport all 49 boxes, 
# rounded to a scale of 4 decimal places (i.e., 1.2345 format).

# for large n, dist of sample mean approaches normal dist
# here we have total pounds are x, and number of samples is n
# where n=49, x=9800
# N(u, s) where u=n*u and s=sqrt(n)*s

import sys
import math
from math import sqrt, pi, exp, erf

param = []

for line in sys.stdin:
    tmp = line.replace('\n','')
    param += list(map(int,tmp.split(' ')))
    
def cdf(u,s,x):
    out = 0.5 * (1 + erf((x-u)/(s*sqrt(2))))
    
    return out
    
n, x = param[1], param[0]
u, s = param[2], param[3]

print(round(cdf(n*u, math.sqrt(n)*s, x),4))