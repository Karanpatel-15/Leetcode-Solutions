class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        res = 0
        
        for i in range(len(nums)):
          mx = nums[i]
          mn = nums[i]
          for j in range(i+1, len(nums)):
            mx = max(mx, nums[j])
            mn = min(mn, nums[j])
            res += mx - mn

        return res
        