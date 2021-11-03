# Objective
# In this challenge, we practice calculating the probability of a compound event. 

# Task
# There are 3 urns labeled X, Y, and Z.

# Urn X contains 4 red balls and 3 black balls.
# Urn Y contains 5 red balls and 4 black balls.
# Urn Z contains 4 red balls and 4 black balls.

# One ball is drawn from each of the 3 urns. 
# What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?

# exhaustive explanation is as follows
# there are 3 combinations of such probability
# (r,r,b), (r,b,r), (b,r,r) where each index corresponds to urn X, Y, and Z
# the probability of the compound event is the sum of 3 events

# 4/7*5/9*1/2 + 4/7*4/9*1/2 + 3/7*5/9*1/2 = 17/42

# following is slight modification of ee3pox's response on HackerRank
import itertools
from fractions import Fraction

X = ["b","b","b","r","r","r","r"]
Y = ["b","b","b","b","r","r","r","r","r"]
Z = ["b","b","b","b","r","r","r","r"]

r = [(i)for i in itertools.product(X,Y,Z)] #permutation without self-pair
e = list(map(lambda x : x.count('r') == 2 and x.count('b') == 1,r))
res = Fraction(e.count(True),len(e)) #fraction object
print(res)