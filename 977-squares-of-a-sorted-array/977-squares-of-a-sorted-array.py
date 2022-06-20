class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = [0]*(len(nums))
        
        l, r = 0, len(nums)-1
        counter = len(nums)-1
        
        while l <= r:
          if abs(nums[r]) >= abs(nums[l]):
            res[counter] = nums[r]**2
            r-=1
          else:
            res[counter] = nums[l]**2
            l+=1
          counter -= 1
        
        return res
        