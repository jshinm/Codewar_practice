# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

# Complexity Analysis
# O(N) Time 
# O(N) Space

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS solution
class Solution:
    def findTarget_BFS(self, root, k):
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: 
                # print(i.val, s)
                return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False
# DFS
    def findTarget_DFS(self, root: TreeNode, k: int) -> bool:
        s = set()
        def helper(root, k):
            if not root: return False
            if k - root.val in s: 
                # print(k,root.val,s)
                return True
            s.add(root.val)
            return(helper(root.left, k) or helper(root.right, k))
        return helper(root, k)

