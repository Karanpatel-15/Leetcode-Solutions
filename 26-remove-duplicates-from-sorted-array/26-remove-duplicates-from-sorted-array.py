class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1
        for i in range(len(nums)-1):
          if(nums[i]!=nums[i+1]):
            nums[l] = nums[i+1]
            l+=1
        return(l)