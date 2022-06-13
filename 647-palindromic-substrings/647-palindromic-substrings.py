class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        
        def helper(l, r):
          counter = 0
          while l >= 0 and r < len(s) and s[l] == s[r]:
            counter += 1
            l-=1
            r+=1
             
          return counter
        
        for i in range(len(s)):
          if i != 0 and s[i] == s[i-1]:
            res += (1 + helper(i-2, i+1))  
          res += (1 + helper(i-1, i+1))
          
        return res