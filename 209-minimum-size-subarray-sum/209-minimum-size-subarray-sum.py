class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        l, r = 0, 0
        m = float("inf")
        total = 0
        while r < len(nums):
          total += nums[r]
          while target <= total:
            m = min(m, r - l + 1)
            total -= nums[l]
            l+=1
          r+=1
            
        if m != float("inf"):
          return m
        else:
          return 0         