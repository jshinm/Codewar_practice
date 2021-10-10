# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #if the question were to indicate the consecutive jumps
        #while loop {run until reach the end OR reach zero that is not the last index}
        #[1,1,1,2] => True
        #[1,10,1] => True
        
        if len(nums) == 1: #single item is always true
            return True
        
        idx = 0
        
        try:            
            while True:
                idx += nums[idx] #move to next index
                
                if idx >= len(nums)-1: #if the next passes the last idx, then it's true
                    return True

                if idx + nums[idx] >= len(nums)-1: 
                    #if the number pointed by the next index is greater than 
                    #or equal to the size of the array, it's true
                    return True                     

                if nums[idx] == 0 and idx != len(nums)-1: 
                    #the only false case is if there's zero prior to reaching the last index
                    return False
                
        except Exception as e:
            print(e)