class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        counter = {}
        res = 0
        for r in range(len(s)):
          counter[s[r]] = 1 + counter.get(s[r], 0)
          
          while (r-l+1) - max(counter.values()) > k:
            counter[s[l]] -= 1
            l+=1
          
          res = max(res, (r-l+1))
          
        return res
            