class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        if len(s) < 4 or len(s) > 12:
          return []
        
        res = []
        
        def backtracking(i, dots, currIP):
          if dots == 4 and i == len(s):
            res.append(currIP[:-1])
            return 
          
          if dots == 4:
            return
          
          for j in range(i, min(i+3, len(s))):
            if int(s[i:j+1]) <= 255 and (i == j or int(s[i]) != 0):
              backtracking(j+1, dots+1, currIP + s[i:j+1] + ".")
            
        
        backtracking(0, 0, "")
        return res
                        
        