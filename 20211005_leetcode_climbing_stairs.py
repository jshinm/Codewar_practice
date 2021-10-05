# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:

# 1 <= n <= 45

# ----------- explantion note -------------

# extend logic manually for n = 4
# 1+1+1+(1)
# 1+2+(1)
# 2+1+(1)
# 1+1+(2)
# 2+(2)
# there's a pattern that for n steps, (n-1)+1 and (n-2)+2 methods are there
# so the equation is f(n) = f(n-1) + f(n-2) where f(n-1) to f(n) is practically 1 step behind 
# so the number of ways in which one can go up one step is constant as can be seen from manual solution
# same is true for f(n-2) to f(n) where ways in which f(n-2) to f(n-1) is excluded in which case 
# the only way to move up 2 steps is by taking 2 steps at a time, thus the total number of ways to go from f(n-2) to f(n) does not change either
# f(n) is then basically f(n-1) + f(n-2) from the examination
# this is basically the fibonacci sequence

class Solution:
    def climbStairsI(self, n: int) -> int:
        #recursive top-down approach
        if n == 1:
            return 1
        elif n == 2:
            return 2

        return self.climbStairsI(n-1) + self.climbStairsI(n-2)

    def climbStairsII(self, n: int) -> int:
        #dynamic programming bottom-up approach
        if n <= 2:
            return n

        ans = [0]
        ans += [1]
        ans += [2]

        for i in range(3, n+1):
            ans += [ans[i-1] + ans[i-2]]
        
        return ans[-1]

