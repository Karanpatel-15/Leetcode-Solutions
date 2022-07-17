class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        if k == 1:
          return 1
        
        counter = 1
        for i in range(2, (n // 2) + 1):
          if n % i == 0:
            counter += 1
            if counter == k:
              return i
                        
        if k == counter+1:
          return n
        else:
          return -1
        
            
        
        
        
        