class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        -4, -1, 1, 2
        
        
        """
              
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
          
            if i > 0 and nums[i] == nums[i-1]:
                continue
          
            l, r = i+1, len(nums)-1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if abs(s-target) < abs(res-target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else: # break early 
                    return res
        return res
            
        return result
          
#         nums.sort()
#         res = nums[0] + nums[1] + nums[2]
        
#         for i in range(len(nums)-2):
#           if i != 0 and nums[i] == nums[i-1]:
#             continue
            
#           l, r = i+1, len(nums)-1
#           while l < r:
#             total = nums[i] + nums[l] + nums[r]
            
#             if total == target:
#               return sum
      
#             if abs(total - target) <  abs(res - target):
#               res = total
            
#             if total < target:
#               l+=1
#             elif total > target:
#               r-=1
          
#         return res
              
        
        
        
        
        