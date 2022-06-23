class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l, r = 0, len(nums)-1
        i = 0
        
        while i <= r:
          temp = nums[i]
          if nums[i] == 0:
            nums[i] = nums[l]
            nums[l] = temp
            l += 1
          if nums[i] == 2:
            nums[i] = nums[r]
            nums[r] = temp
            r-=1
            i-=1
          i+=1

            
        