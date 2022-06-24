class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        last = {}
        for i, l in enumerate(s):
          last[l] = i
        
        size = end = 0
        res = []
        
        for i in range(len(s)):
          size += 1
          end = max(end, last[s[i]])

          if i == end:
            res.append(size)
            size = 0
          
          
        return res
        