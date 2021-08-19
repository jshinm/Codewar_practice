# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

# Complexity Analysis

# Time Complexity: O(log(x)). There are roughly log10(x) digits in x.
# Space Complexity: O(1).

class Solution:
    def reverse(self, x: int) -> int:

        temp = 0
        
        if x >= 0:
            temp = int(str(x)[::-1])
        elif x < 0:
            temp = -int(str(x)[::-1][:-1])
        
        if temp >= -2**31 and temp <= 2**31 - 1:
            return temp
        else:
            return 0

if __name__ == "__main__":

    sol = Solution()
    print( sol.reverse(-1253548) )