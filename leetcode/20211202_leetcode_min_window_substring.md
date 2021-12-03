# Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Constraints:
* m == s.length
* n == t.length
* 1 <= m, n <= 105
* s and t consist of uppercase and lowercase English letters.

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        brute force
        1. iterate over s and find the first subsequence that contains t
        2. starting from the last char in s that cintains char in t, try finding the second
        3. find the shortest substring
        
        TC: O(m*n)
        
        hashmap method
        1. linear scan the s and store the index of each char of t
        
        s = "ADOBECODEBANC", t = "ABC"
        
        A: [0, 10]
        B: [3, 9]
        C: [5, 12]
        
        2. find all linear sequence that contains all char of t and has the shortest length
        
        [0,3,5],[3,5,10],[5,9,10],[9,10,12]
        
        edge case: if t.length > s.length, return ''
        '''
        #edge case
        if len(t) > len(s):
            return ''
        
        imap = {} #hashmap for indexing
        cmap = {} #hashmap for tracking counts
        min_key = '' #key for smallest number
        min_len = len(s)
        out = '' #char output
        done = False
        
        for i, c in enumerate(s):
            if c in t and c in imap:
                imap[c].append(i)
            elif c in t and not c in imap:
                imap[c] = [i]
                cmap[c] = 0
                
        while not done:
            tmp = [] #temp sequence of indices
            min_num = len(s)+1 #initialize current smallest number
            
            for c, n in cmap.items():
                if n+1 > len(imap[c]):
                    done = True
                    break
                    
                if min_num > imap[c][n]:
                    min_num = imap[c][n]
                    min_key = c
                    
                tmp.append(imap[c][n]) #store index of each char from s
            
            # print(s, t, min_num, min_key)
            
            if not done:
                try:
                    cmap[min_key] += 1 #increase count
                except:
                    return ''
                
                tmin, tmax = min(tmp), max(tmp)

                if min_len > tmax-tmin:
                    min_len = tmax-tmin
                    iout = (tmax, tmin) #temp save of current sequence

        out = s[tmin:tmax+1] #translate index into char
        
        return out
```