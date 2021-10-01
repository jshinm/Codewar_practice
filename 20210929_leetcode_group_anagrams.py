# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from typing import List

class Solution:
    def groupAnagrams_I(self, strs: List[str]) -> List[List[str]]:
        #brute force solution
        #take each item sort to check their equality
        #then add to a new nested list
        #original list is popped
        #TC: n^2, worst case
        
        ans = []

        while strs != []:
            
            temp_i = strs.pop()
            temp_lst = [temp_i]

            temp_i = ''.join(sorted(temp_i))

            for i in range(len(strs)-1, -1, -1): 
                #(n, 0) => [n-1, -1]
                #going reverse will allow correct book keeping of the index

                if len(strs[i]) != len(temp_i):
                    continue

                if ''.join(sorted(strs[i])) == temp_i:
                    temp_lst.append(strs.pop(i))

            ans.append(temp_lst)

        return ans
        
        def groupAnagrams_II(self, strs: List[str]) -> List[List[str]
        
        #hashmap solution
        
        ans = {}
        
        for i in strs:
            temp = ''.join(sorted(tuple(i))) #unique ordered key
            ans[temp] = ans.get(temp, []) + [i] #values of the same key falls under the same key
            
        return list(ans.values()) #output is a list
