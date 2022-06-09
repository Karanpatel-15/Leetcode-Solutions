class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = set(nums)
        res = 0
        
        for num in nums:
          if num-1 not in s:
            count = 1
            temp = num + 1
            while temp in s:
              count += 1
              s.remove(temp)
              temp += 1
            
            res = max(count, res)
        
        return res
          