class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = 0
        subString = set()
        mx = 0
        
        for r in range(len(s)):
          
          while s[r] in subString:
            subString.remove(s[l])
            l+=1
          
          subString.add(s[r])
          mx = max(mx, len(subString))
          
        return mx
        
          
        