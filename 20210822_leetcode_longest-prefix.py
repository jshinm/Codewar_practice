# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Complexity Analysis

# Time complexity : O(S) , where S is the sum of all characters in all strings.
# Space complexity : O(1). We only used constant extra space.

class Solution:
    #horizontal scanning
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) != 0:
            prefix = strs[0]
        else:
            return ""
        
        for i in strs[1:]:
            
            temp = ""
            
            for n, letter in enumerate(prefix):
                
                if len(i) < n+1:
                    break
                
                # print(len(i), i[n], letter)
                
                if i[n] == letter:
                    temp += letter
                else:
                    break

            prefix = temp
                
        return prefix