class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        red = 0
        white = 0
        blue = 0
        for c in nums:
          if c == 0:
            red+=1
          elif c == 1:
            white+=1
          else:
            blue+=1
        
        counter = 0
        while red != 0:
          nums[counter] = 0
          red -= 1
          counter+=1
        while white != 0:
          nums[counter] = 1
          white -= 1
          counter+=1

        while blue != 0:
          nums[counter] = 2
          blue -= 1
          counter+=1

            
        