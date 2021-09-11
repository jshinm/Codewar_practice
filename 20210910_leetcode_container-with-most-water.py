# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

class Solution:
    #brute force
    def maxArea(self, height: List[int]) -> int:

        maxarea = 0

        for i, ai in enumerate(height):
            for j, aj in enumerate(height):
                if ai >= aj and min(ai,aj) * abs(j-i) > maxarea:
                    maxarea = min(ai,aj) * abs(j-i)

        return maxarea