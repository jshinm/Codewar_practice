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
        edge case2: if t.length == s.length, check if t E s
        '''
        #edge case1
        if len(t) > len(s):
            return ''
        
        #edge case2
        elif len(t) == len(s):
            tlst = list(t)
            slst = list(s)
            
            tlst.sort()
            slst.sort()
            
            if slst == tlst:
                return s
            else:
                return ''
        
        imap = {} #hashmap for indexing
        cmap = {} #hashmap for tracking counts
        dmap = {} #hashmap for duplicates
        min_key = '' #key for smallest number
        min_len = len(s)
        done = False
        
        for i, c in enumerate(s):
            if c in t and c in imap:
                imap[c].append(i)
            elif c in t and not c in imap:
                imap[c] = [i]
                cmap[c] = 0
                
        for c in t:
            if c not in dmap:
                dmap[c] = 0
            else:
                dmap[c] += 1
                
        while not done:
            tmp = [] #temp sequence of indices
            min_num = len(s)+1 #initialize current smallest number
            
            for r in range(dmap[c]+1): #when repeating char exists
                for c, n in cmap.items():
                    if n+1+r > len(imap[c]):
                        done = True
                        break

                    if min_num > imap[c][n+r]:
                        min_num = imap[c][n+r]
                        min_key = c

                    tmp.append(imap[c][n+r]) #store index of each char from s

                if not done:
                    try:
                        cmap[min_key] += 1 #increase count
                    except:
                        return ''

                    tmin, tmax = min(tmp), max(tmp)

                    if min_len > tmax-tmin:
                        min_len = tmax-tmin
                        iout = (tmin, tmax) #temp save of current sequence
        
        if iout[0] != iout[1]:
            return s[iout[0]:iout[1]+1] #translate index into char
        else:
            return ''
```