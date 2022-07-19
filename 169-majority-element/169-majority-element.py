from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = Counter(nums)
        
        for n in s:
          if s[n] > (len(nums)//2):
            return n
                
        