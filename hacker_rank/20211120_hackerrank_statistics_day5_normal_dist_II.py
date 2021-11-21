# Objective
# In this challenge, we go further with normal distributions.

# Task
# The final grades for a Physics exam taken by a large group of students have a mean of u=70 and a standard deviation of s=10. 
# If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

# Scored higher than 80 (i.e., have a grade > 80)?
# Passed the test (i.e., have a grade >= 60)?
# Failed the test (i.e., have a grade < 80)?

# Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

# Input Format
# There are 3 lines of input (shown below):
# The first line contains 2 space-separated values denoting the respective mean and standard deviation for the exam. 
# The second line contains the number associated with question 1. 
# The third line contains the pass/fail threshold number associated with questions 2 and 3.

# Output Format
# There are three lines of output. Your answers must be rounded to a scale of 3 decimal places (i.e., 1.234 format):

# On the first line, print the answer to question 1.
# On the second line, print the answer to question 2.
# On the third line, print the answer to question 3.

# upper limit not known thus 1-cdf(x)

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
    
u, s = param[0][0], int(param[0][1])
print(round((1-cdf(u,s, 80))*100,2))
print(round((1-cdf(u,s, 60))*100,2))
print(round((cdf(u,s, 60))*100,2))