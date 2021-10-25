# Objective
# In this challenge, we practice calculating the mean, median, and mode. 

# Task
# Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. 
# If your array contains more than one modal value, choose the numerically smallest one.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

for line in sys.stdin:
    out = line.rstrip().split(' ')
    
out = sorted(list(map(int, out)))
N = len(out)

print(sum(out)/N) #mean

if N % 2 == 0:
    idx = [int(N/2-1), int(N/2)]
elif N % 2 == 1:
    idx = [int(N/2)]

num = [out[i] for i in idx]
print(sum(num)/len(num)) #median

dic = {}

for i in out:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

# the output list is already sorted, so sorted by freq once more will be enough
print(sorted(dic.items(), key=lambda x:x[1], reverse=True)[0][0]) #mode