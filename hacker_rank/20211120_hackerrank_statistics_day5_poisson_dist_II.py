# Objective
# In this challenge, we go further with Poisson distributions.

# Task
# The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:

# The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is C_A=160+40X^2.
# The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is C_B=128+40Y^2.
# Assume that the repairs take a negligible amount of time and the machines are maintained nightly 
# to ensure that they operate like new at the start of each day. 
# Find and print the expected daily cost for each machine.

# Input Format
# A single line comprised of 2 space-separated values denoting the respective means for A and B:

# Output Format
# There are two lines of output. Your answers must be rounded to a scale of 3 decimal places (i.e., 1.234 format):

# On the first line, print the expected daily cost of machine A.
# On the second line, print the expected daily cost of machine B.

# One doesn't need to actually calculate the Poisson distribution (and for that matter, we do not know k anyway). 
# What one should do is realise that for some random Poisson variable, X, the expectation value and the variance are:

# E[X] = lambda
# and
# var[X] = lambda

# var[X] = E[X^2] + E[X]^2
# E[X^2] = var[X] + E[X]^2
#        = lambda + lambda^2

# The question specifically asks for the average during the day (with each day being independent of each other), 
# and hence the expectation value is that, the average of all possible events over the day.

# As given, daily cost C_A is 160+40X^2, thus its expected value would be
# 160+40*E[X^2], which is solved as above for poisson distribution

import sys
import math

param = []

for line in sys.stdin:
    tmp = line.replace('\n', '')
    param += list(map(float, tmp.split(' ')))

print(round(160+40*(param[0]+param[0]**2),3))
print(round(128+40*(param[1]+param[1]**2),3))