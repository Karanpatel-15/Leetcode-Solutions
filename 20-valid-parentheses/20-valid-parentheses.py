class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        brackets = {"(":")","{":"}","[":"]"}
        
        for b in s:
          if b in brackets:
            stack.append(b)
          elif len(stack) != 0 and b == brackets[stack.pop()]:
            continue
          else:
            return False
        
        return len(stack) == 0
          