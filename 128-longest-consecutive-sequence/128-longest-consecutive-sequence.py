class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = set(nums)
        
        mx = 0
        
        for n in nums:
          curr = n+1
          total = 1
          while curr in s:
            total += 1
            s.remove(curr)
            curr+=1
          curr = n-1
          while curr in s:
            total += 1
            s.remove(curr)
            curr-=1
              
          mx = max(total, mx)
        
        
        return mx
        
        