# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at
# an unknown pivot index k (1 <= k < nums.length) such that the resulting
# array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1


# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

from typing import List

class Solution:
    def search_I(self, nums: List[int], target: int) -> int:
        #pythonic simple solution
        try:
            return nums.index(target)
        except Exception as e:
            print(e)
            return -1

    def search_II(self, nums: List[int], target: int) -> int:
        #binary search method
        #3 pointers: l, m, r where m is (l+r)/2
        #between l & m: 
        #   there exists target => bring r to m otherwise bring l to m
        #between m & r:
        #   there exists target => bring l to m otherwise bring r to m

        if nums == []:
            return nums

        if target not in nums: #edge case
            return -1

        l = 0
        r = len(nums)-1

        while l <= r:

            m = int((l+r) / 2)

            if nums[m] == target: #if target found, return m
                return m

            if nums[l] <= nums[m]: 
                #if left search field is sorted

                if nums[l] <= target <= nums[m]: #if target exists
                    r = m
                else:
                    l = m + 1 #immediately outside of the search parameter
            else: 
                #outside of the sorted left search field
                #there exists three conditions:
                #1. unsorted left search field (ie rotated)
                #2. sorted right search field
                #3. unsorted right search field
                if nums[m] <= target <= nums[r]: #if target exists
                    l = m
                else:
                    r = m - 1 #immediately outside of the search parameter

        return -1

sol = Solution()
val = sol.search_I([1,3,5,2,6,7], 4)
print(val)