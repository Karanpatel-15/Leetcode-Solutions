class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        counter = 0
        
        for i in range(32):
          counter += (n >> i) & 1
          
        return counter