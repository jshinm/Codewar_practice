# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force
        #O(N^3)
        ans = []
        duplicate = False

        for i, ai in enumerate(nums):
            for j, aj in enumerate(nums[i+1:]):
                for k, ak in enumerate(nums[i+1:][j+1:]):
                    if ai + aj + ak == 0:
                        for ans_i in ans:
                            temp = ans_i
                            temp2 = [ai,aj,ak]

                            temp.sort()
                            temp2.sort()
                            
                            if temp == temp2:
                                duplicate = True
                                break

                        if duplicate:
                            duplicate = False
                        else:
                            ans.append([ai,aj,ak])

        return ans