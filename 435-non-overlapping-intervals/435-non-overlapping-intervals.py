class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        
        [[0,2],[1,3],[2,4],[3,5],[4,6]]
        
        """
        
        intervals.sort(key=lambda x:x[0])
        
        prev = intervals[0]
        
        res = 0
        
        for curr in intervals[1:]:
          if prev[1] > curr[0]:
            res += 1
            if curr[1] < prev[1]:
              prev = curr
          else:
            prev = curr
        
        return res
          
        