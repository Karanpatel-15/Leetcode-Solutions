class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        [7,1,5,3,6,4]
             ^
           ^
        """
        
        res = 0
        l, r = 0, 0
        while r < len(prices):
          if prices[r] > prices[l]:
            res = max(res, prices[r] - prices[l])
            r+=1
          else:
            l = r
            r+=1
            
        return res
            
          