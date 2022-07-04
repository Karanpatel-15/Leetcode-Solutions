class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        mapping = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        res = 0
        i = 0
        while i < len(s):   
          if i < len(s)-1:
            letters = s[i:i+2] 
            if letters in mapping:
              res += mapping[letters]
              i += 2
              continue
              
          res += mapping[s[i]]
          i += 1
        
        return res
            
          
            
        