# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# Example 3:

# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]
# Example 4:

# Input: intervals = [[1,5]], newInterval = [2,3]
# Output: [[1,5]]
# Example 5:

# Input: intervals = [[1,5]], newInterval = [2,7]
# Output: [[1,7]]
 

# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #iterate over intervals and place the new list and if overlap conditions are met then merge
        #the intervals is non-overlapping nested list
        #iterate over intervals and place the new list and if overlap conditions are met then merge
        #the intervals is non-overlapping nested list
        #TC: O(N) - linear search only
        
        #alternatively, add newInt to the intervals, then sort (TC: n log n), followed by linear overlap search

        #the following is the mix of linear search followed by sort, thus TC: n log n
        
        out = []
        merge = None #temp storage for merging list
        
        if intervals == []: #edge case: empty
            return [newInterval]
        
        for interval in intervals:

            if interval[1] < newInterval[0] or interval[0] > newInterval[1]:
                if merge:
                    out.append(merge)
                    merge = []
                out.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]),
                                max(interval[1], newInterval[1])]
                merge = newInterval
                
        if merge == []:
            pass
        elif merge == None:
            out.append(newInterval)
        else:
            out.append(merge)
            
        out.sort(key=lambda x: x[0]) #TC: O(N log N)
            
        return out