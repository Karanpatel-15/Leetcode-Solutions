class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        currSum = 0
        realSum = 0
        
        for i in range(len(nums)):
          currSum += nums[i]
          realSum += i+1
          
        return realSum - currSum