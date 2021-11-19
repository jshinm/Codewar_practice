# Objective
# In this challenge, we go further with binomial distributions. 

# Task
# A manufacturer of metal pistons finds that, on average, 12% of the pistons 
# they manufacture are rejected because they are incorrectly sized. 
# What is the probability that a batch of 10 pistons will contain:

# No more than 2 rejects?
# At least 2 rejects?

# Input Format
# A single line containing the following values (denoting the respective 
# percentage of defective pistons and the size of the current batch of pistons):

# Output Format
# Print the answer to each question on its own line:
# The first line should contain the probability that a batch of  pistons will contain no more than  rejects.
# The second line should contain the probability that a batch of  pistons will contain at least  rejects.
# Round both of your answers to a scale of 3 decimal places (i.e., 1.234 format).

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math

# no more than 2 rejects: P(no reject) + P(1 reject) + P(2 rejects)
# at least 2 rejects: 1 - [P(no reject) + P(1 reject)]

param = []

for line in sys.stdin:
    tmp = line.replace('\n','')
    param.append(list(map(float, tmp.split(' '))))

def binom(x,n,p):
    return math.comb(n,x) * p**x * (1-p)**(n-x)

def prob(b,g):
    p = 0.12 #prob of reject
    c = 0 #cumulative prob
    
    #no more than 2 rejects
    for x in range(0,3):
        c += binom(x,10,p)
    
    print(round(c,3))
    
    c = 0 #reset value 
    #at least 2 rejects
    for x in range(0,2):
        c += binom(x,10,p)
    
    print(round(1 - c, 3))
    
for par in param:
    prob(par[0], par[1])