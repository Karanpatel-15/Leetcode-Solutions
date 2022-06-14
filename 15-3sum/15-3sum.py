class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        [-4,-1,-1,0,1,2]
        
        """
        
        nums.sort()
        res = []
        
        for i in range(0, len(nums)-2):
          if i != 0 and nums[i] == nums[i-1]:
            continue
            
          target = 0 - nums[i]
          
          l, r = i+1, len(nums)-1
          
          while l < r:
            total = nums[l] + nums[r]
            
            if total == target:
              res.append([nums[i],nums[l],nums[r]])
              l+=1
              while l < r and nums[l] == nums[l-1]:
                l+=1
            elif total > target:
              r-=1
            elif total < target:
              l+=1
              
        return res
          
          
          
        