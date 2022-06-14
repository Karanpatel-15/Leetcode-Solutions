class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        res = 1
        lmap = {}
        l = 0
        
        for r in range(len(s)):
          letter = s[r]
          
          lmap[letter] = lmap.get(letter, 0) + 1
          
          while (r-l+1) - max(lmap.values()) > k:
              lmap[s[l]] -= 1
              l+=1
          res = max(res, (r-l+1))
        return res
            