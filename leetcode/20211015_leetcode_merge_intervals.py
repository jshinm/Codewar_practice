# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #if end_i >= start_i+1, then they overlaps
        #but must be sorted => O(nlog(n))
        #TC: O(N) of linear scan < O(N) of python list sort
        
        ans = []
        
        if len(intervals) == 1:
            return intervals
        
        intervals.sort()
        
        s_i, e_i = intervals.pop(0)
        
        for int_i in intervals:
            temp_s, temp_e = int_i
            
            if e_i >= temp_s:
                s_i = [s_i,temp_s][s_i >= temp_s] #whichever starts smaller
                e_i = [e_i,temp_e][e_i <= temp_e] #whichever ends larger
            else:
                ans.append([s_i, e_i])
                s_i, e_i = temp_s, temp_e
                
        ans.append([s_i, e_i])
                
        return ans