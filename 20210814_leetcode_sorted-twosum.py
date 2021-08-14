# Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1
        
        while True:
            total = numbers[l] + numbers[r]
            
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            elif total == target:
                return [l+1, r+1]
            else:
                print("error")
                break

if __name__ == "__main__":
    sol = Solution()
    print ( sol.twoSum([2,7,11,15], 9) )