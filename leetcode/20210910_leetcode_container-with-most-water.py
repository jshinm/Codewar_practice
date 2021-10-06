# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

from typing import List

class Solution:
    #brute force
    #O(N^2)
    def maxArea_1(self, height: List[int]) -> int:

        maxarea = 0

        for i, ai in enumerate(height):
            for j, aj in enumerate(height):
                if ai >= aj and min(ai,aj) * abs(j-i) > maxarea:
                    maxarea = min(ai,aj) * abs(j-i)

        return maxarea

    # two pointers
    # move left if the right is larger than the left because any movement from the right would not increase the volume
    # move right if the left is larger than the right because any bars taller than the left could yield increase in volume
    # O(N)
    def maxArea_2(self, height: List[int]) -> int:

        maxarea = 0
        lft = 0
        rht = len(height)-1

        while (lft != rht):
            if height[lft] >= height[rht]:
                temp = height[rht] * abs(rht-lft)
                rht -= 1
            else:
                temp = height[lft] * abs(rht-lft)
                lft += 1

            if temp > maxarea:
                maxarea = temp

        return maxarea