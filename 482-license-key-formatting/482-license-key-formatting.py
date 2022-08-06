class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        cur = 0
        res = ""
        for c in s[::-1]:
            if c == '-': 
              continue
            if cur == k: 
                res = "-" + res
                cur = 0
            res = c.upper() + res
            cur += 1
        return res
        