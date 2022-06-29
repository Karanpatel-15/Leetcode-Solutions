class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
          curr = intervals[i]
          prev = res[-1]
          
          if prev[1] >= curr[0]:
            prev[1] = max(curr[1], prev[1])
            res[-1] = prev
          else:
            res.append(curr)
        return res
          