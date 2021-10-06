# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true

class Solution:
    #hashmap solution
    #TC: O(N)
    def isValid_I(self, s: str) -> bool:

        dicts = {'{':'}', '[':']', '(':')'}
        lst = []

        for char in s:
            if char in dicts:
                lst.append(char)
            elif char in dicts.values() and lst != []:
                temp = [key for key, value in dicts.items() if value == char][0]
                if temp == lst[-1]:
                    lst.pop()
                else:
                    return False
            else: #edge case when only closed
                return False

        if lst != []: #edge case when pair not found
            return False

        return True

    #reversed hashmap version
    #TC: N(O)
    def isValid_II(self, s: str) -> bool:
        
        dicts = {'}':'{', ']':'[', ')':'('} #reversed key:value pair
        lst = []

        for char in s:
            if char in dicts.values():
                lst.append(char)
            elif lst == [] or dicts[char] != lst.pop(): #given that s is only consisting of parenthesis the `lst` should not be empty when the sequence is properly ordered; otherwise, `lst` will have to be popped and popped list is not matching the hashmap value, then the ordering is incorrect, thus for these two cases, returning false
                return False

        if lst != []: #edge case when pair not found
            return False

        return True #if all cases pass, return true