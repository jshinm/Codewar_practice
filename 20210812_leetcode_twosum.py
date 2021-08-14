# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

from typing import List

# brute force method O(n*n) at worst case scenario
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i , j]

# hashmap method
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
        return []





if __name__ == "__main__":
    sol = Solution()
    print( sol.twoSum([1,2,3,5,4,3,2,6,7,4,3],8) )

    sol = Solution2()
    print( sol.twoSum([1,2,3,5,4,3,2,6,7,4,3],8) )