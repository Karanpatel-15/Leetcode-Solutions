class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        lastPos = {}
        
        for i, l in enumerate(s):
          lastPos[l] = i
        
        res = []
        end = lastPos[s[0]]
        size = start = 0
        for i, l in enumerate(s):
          size += 1
          end = max(end, lastPos[l])
          if i == end:
            res.append(size)
            size = 0
          
        return res
        