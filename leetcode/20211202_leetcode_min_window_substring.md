# Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Constraints:
* m == s.length
* n == t.length
* 1 <= m, n <= 105
* s and t consist of uppercase and lowercase English letters.

## Efficient LC Solution (O(S+T) where S, T are length of the string)
```python
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
```

## Hashmap-based Solution (TLE)

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
        
        edge case1: if t.length > s.length, return ''
        edge case2: if t.length == s.length, check if t E s
        edge case3: edge case for the following two cases
        s = "abbbb", t = "aa" AND s = "ab", t = "a"
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
            
        #edge case 3
        ss = list(s)
    
        for c in list(t):
            if c in ss:
                ss.remove(c)
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
            
            for c, n in cmap.items():
                for r in range(dmap[c]+1): #when repeating char exists
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
                    iout = (tmin, tmax) #export range
        
        #all else return output
        return s[iout[0]:iout[1]+1] #translate index into char