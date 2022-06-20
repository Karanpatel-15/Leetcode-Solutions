class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        r = 1
        while r < len(nums):
          if nums[l] != 0:
            l += 1
            r += 1
          elif nums[r] == 0:
            r+=1
          else:
            temp = nums[r]
            nums[r] = nums[l]
            nums[l] = temp
        