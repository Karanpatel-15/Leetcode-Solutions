class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        s = s.strip()
        
        if len(s) == 0:
          return 0
        
        sign = 1
        if s[0] == "-" or s[0] == "+":
          if s[0] == "-":
            sign = -1
          s = s[1:]
          
        print(s)
          
        
        res, i = 0, 0
        
        while i < len(s) and s[i].isnumeric():
          res = res*10 + int(s[i])
          i+=1
      
        return max(-2**31, min(sign*res, 2**31-1))
      
          
          

        
        
        
        