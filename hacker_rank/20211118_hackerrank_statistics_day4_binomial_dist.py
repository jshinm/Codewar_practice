# Objective
# In this challenge, we learn about binomial distributions. Check out the Tutorial tab for learning materials!

# Task
# The ratio of boys to girls for babies born in Russia is 1.09:1. 
# If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters. 
# Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

# Input Format
# A single line containing the following values:
# 1.09 1

# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format
# Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math

# prob of having boys is 1.09/2.09, and for girls 1.00/2.09
# at least 3 boys is P(3 boys) + P(4 boys) + P(5 boys) + P(6 boys)
# alternatively, 1-P(of not having 3 boys)
# 1-(P(4 girls)+P(5 girls)+P(6 girls))
# then it boils down to calculating the cumulative probability of binomial distribution
# b(x,n,p) = n choose x * p^x * q^(n-x)

param = []

for line in sys.stdin:
    tmp = line.replace('\n','')
    param.append(list(map(float, tmp.split(' '))))

def binom(x,n,p):
    return math.comb(n,x) * p**x * (1-p)**(n-x)
    
def prob(b,g):
    p = b/(b+g)    
    c = 0
    
    for x in range(3,7):
        c += binom(x,6,p)
    
    return round(c,3)
    
for par in param:
    print(prob(par[0], par[1]))