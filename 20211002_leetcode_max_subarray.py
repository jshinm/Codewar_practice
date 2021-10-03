# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

from typing import List

class Solution:
    def maxSubArrayI(self, nums: List[int]) -> int:
        
        #brute force
        #TC: O(n^2)
        
        max_num = -10**4
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)+1):
                temp = sum(nums[i:j])
                
                if temp > max_num:
                    max_num = temp
                    
        return max_num

    def maxSubArrayII(self, nums: List[int]) -> int:
        #double max method
        #TC: O(N)
               
        max_val = cur_val = nums[0] 
        #[10,-11,10] => rather restart at i = 2
        #[1,2,-1,10] => -1 can be ignored
        #[-10,10,10] => -10 is passed
        #[9,-1,10]   => -1 is kept
        #[9,-1,-1,-1]=> cur_val keeps all sequence, but max_val only keeps the 9
        
        #thus cur_val only evaluates whether sum up to ith is greater than the ith num
        #as long as ith num is less than the sum up to ith sequence, sequence is kept        
        
        for num in nums[1:]:
            cur_val = max(cur_val + num, num)
            max_val = max(cur_val, max_val)
            
        return max_val

    def maxSubArrayIII(self, nums: List[int]) -> int:
        #no max method
        #TC: O(N)
               
        max_val = nums[0]
        cur_val = 0
        
        #if cur_val is negative, not worth it to start with neg number, thus reset every time
        #but the max_val is still kept track of 
        
        for num in nums:
            
            cur_val += num
            
            if cur_val > max_val:
                max_val = cur_val

            if cur_val < 0:
                cur_val = 0

        return max_val