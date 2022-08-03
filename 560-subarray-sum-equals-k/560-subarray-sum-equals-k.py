class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        cnt = {0:1}
        res = s = 0
        for i in nums:
          s += i
          
          if s - k in cnt:
            res += cnt[s-k]
          
          cnt[s] = cnt.get(s, 0) + 1
          
        return res            