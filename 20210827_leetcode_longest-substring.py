# Given a string s, find the length of the longest substring without repeating characters.

# Two pointer solution where each string is stored in a hash table from which each char is used as a key and its location is stored as corresponding value.
# If there exists multiple same char in a given string, the second char location replaces the preceding one.
# As long as the char has not been encountered, the max_length is updated according to `i - start(the last repeating character) + 1`

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        used = {}
        max_length = 0
        start = 0
        
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i

        return max_length