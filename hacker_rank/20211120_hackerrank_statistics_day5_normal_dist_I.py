# Objective
# In this challenge, we learn about normal distributions.

# Task
# In a certain plant, the time taken to assemble a car is a random variable, X, 
# having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. 
# What is the probability that a car can be assembled at this plant in:

# Less than 19.5 hours?
# Between 20 and 22 hours?

# Input Format
# The first line contains 2 space-separated values denoting the respective mean and standard deviation for X. 
# The second line contains the number associated with question 1. 
# The third line contains 2 space-separated values describing the respective lower and upper range boundaries for question 2.

# Output Format
# There are two lines of output. Your answers must be rounded to a scale of 3 decimal places (i.e., 1.234 format):

# On the first line, print the answer to question 1 (i.e., the probability that a car can be assembled in less than 19.5 hours).
# On the second line, print the answer to question 2 (i.e., the probability that a car can be assembled in between 20 to 22 hours).

# normal equation N(u,s) = 1/(s*sqrt(2pi))*e^-((x-u)^2/(2s^2))
# cdf = 1/2*(1+erf((x-u)/(s*sqrt(2))))

import sys
import math
from math import sqrt, pi, exp, erf

param = []

for line in sys.stdin:
    tmp = line.replace('\n','')
    param.append(list(map(float,tmp.split(' '))))
    
def gauss(u,s,x):
    out = 1/(s*sqrt(2*pi)) * exp(-(x-u)**2/(2*s**2))
    
    return out

def cdf(u,s,x):
    out = 0.5 * (1 + erf((x-u)/(s*sqrt(2))))
    
    return out
    
u, s = param[0][0], param[0][1]

print(round(cdf(u,s, 19.5),3))
print(round(cdf(u,s, param[2][1]) - cdf(u,s, param[2][0]),3))