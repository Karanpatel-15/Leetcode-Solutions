class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if len(intervals) == 1:
          return [intervals[0]]
              
        intervals.sort(key=lambda x:x[0])
        
        res = []
        prev = intervals[0]
        
        for i in range(1, len(intervals)):
          curr = intervals[i]
          
          if prev[1] >= curr[0]:
            prev[1] = max(curr[1], prev[1])
          else:
            res.append(prev)
            prev = curr
            
          if i == len(intervals)-1:
              res.append(prev)
            
        
          
            
        return res