class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = [1]
        total = 0
        
        for i in range(1, len(s)):
          if s[i] != s[i-1]:
            res.append(1)
          else:
            res[-1] += 1
            
        for i in range(1, len(res)):
          total += min(res[i], res[i-1])
        
        return total