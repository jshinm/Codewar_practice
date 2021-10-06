# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
# Example 4:

# Input: candidates = [1], target = 1
# Output: [[1]]
# Example 5:

# Input: candidates = [1], target = 2
# Output: [[1,1]]


# Constraints:

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500

# Time complexity is O(N^target) where N is a length of candidates array.
# Space complexity is O(target).

# This is worst case and without any optimization, like moving position forward and sorting to stop early.
# Just assuming that each recursive step we go over all existing candidates, so base N.
# And go as deep as target in our recursive calls (if candidates are close to 1), so power of target.
# You can mention that this is worst case and optimizations can make time complexity a little better, for interview I think this should be enough.

# DFS vs backtracking
# I think the difference is pruning of tree. Backtracking can stop (finish) searching certain branch by checking the given conditions 
# (if the condition is not met). However, in DFS, you have to reach to the leaf node of the branch to figure out 
# if the condition is met or not, so you cannot stop searching certain branch until you reach to its leaf nodes.

# Difference 1:
# DFS handles an explicit tree.While Backtracking handles an implicit tree

# Difference 2:
# Depth First Search is a special type of backtracking algorithmic design paradigm where the process of backtracking takes place in the leaf nodes. 
# In case of backtracking,the algorithm also rejects the useless branch of the state-space tree.This is why DFS maintains the entire tree structure 
# while Backtracking maintaines a pruned tree

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtrack solution
        # TC, SC: O(2^N)
        ans = []
        self.backtrack(ans, candidates, [], target)
        return ans

    def backtrack(self, lst, nums, tree, target):

        if target < 0: #preventing from going further recursion
            return

        if target == 0:
            lst.append(tree)
            return

        for i in range(len(nums)):
            if nums[i] > target:  # prevent constructing a complete tree
                continue  # prunes sub-branches stemming from what should not have gone beyond the conditional 
                          # (e.g. [1,2,3,4], 6; at [1,2,3], there's no need to make recursion for [1,2,3,4], 
                          # this last round of recursion involves the most numbers, thus makes it faster to run)
            self.backtrack(lst, nums[i:], tree + [nums[i]], target - nums[i])

class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #dfs solution
        def dfs(target, tree, start):

            if target == 0:
                lst.append(tree[:]) #tree[:] not tree
                return

            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    tree.append(candidates[i])
                    dfs(target-candidates[i], tree, i) #duplicate allows thus i and not i+1
                    tree.pop()
                else:
                    break #prevent further growth of tree

        lst = []
        candidates.sort()
        dfs(target, [], 0)
        return lst

sol = Solution()
lst = sol.combinationSum([2, 3, 6, 7], 7)
print(lst)