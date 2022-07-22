class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = nums[0]
        l, r = 0, len(nums)-1
        
        while l <= r:
          if nums[l] <= nums[r]:
            res = min(res, nums[l])
            break
            
          m = (l+r)//2
          res = min(res, nums[m])
          if nums[l] <= nums[m]:
            l = m + 1  # check right side
            # if nums[m] > nums[l]:
            #   return nums[l]
          else:
            r = m - 1  # check left side
            # if nums[r] > nums[m]:
            #   return nums[m]
            
        return res
          
          
          