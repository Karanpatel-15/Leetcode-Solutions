class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        
        [[0,2],[1,3],[2,4],[3,5],[4,6]]
        
          ---
           ---
            ---
             ---
              ---
        """
        res = 0
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]
        for i in range(1, len(intervals)):
          curr = intervals[i]
          if curr[0] < prev[1]:
            res += 1
            if curr[1] < prev[1]:
              prev = curr
          else:
            prev = curr
          
        return res
        